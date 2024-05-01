import logging
import os

import wx
from threading import Condition
from core.definition.yamlro import YamlRO
from core.loop import Loop
from core.loopparam import LoopParam
from core.processor import Processor
from core.task import Task
from mvp.presenter.event.PETPEvent import PETPEvent
from mvp.view.PETPView import PETPView
from utils.DateUtil import DateUtil
from utils.OSUtils import OSUtils

"""
Execution 1:n Task
"""


class Execution:

    def __init__(self, execution: str, lt: list, lps: list = []):
        self.execution = execution
        self.list = lt
        self.loops = lps

    def set_should_be_stop(self, stopOrNot: bool):
        self.should_be_stop = stopOrNot

    def run(self, initial_data: dict, condition: Condition, view: PETPView) -> dict:
        data_chain = initial_data

        lp: LoopParam = LoopParam(self.list)
        self.set_should_be_stop(False)

        if hasattr(self, 'loops'):
            self.loops.sort(key=lambda loop: loop.get_attribute('task_start'))

        while lp.has_next():

            if self.should_be_stop:
                logging.info(f'Execution: [ {self.execution} ] is manually stop at task: {lp.get_sequence()}')
                return data_chain

            current_loop: Loop = self.find_current_loop(lp.get_sequence())
            lp.init_loop(current_loop)

            if lp.is_loop_start:
                lp.setup_loop_start(data_chain)

            # process start -----
            task: Task = self.initTask(data_chain, lp.current_index, lp.get_sequence())
            processor: Processor = self.initiProcessor(task, view, current_loop, lp.is_loop_execution, condition)

            self.log_start_process(current_loop, lp, processor, task, view)

            # * main process *
            processor.do_process()

            task.end = DateUtil.get_now_in_str("%Y-%m-%d %H:%M:%S")

            self.log_end_process(current_loop, lp, processor, task, view)
            # process end ----

            if lp.is_loop_end:
                lp.setup_loop_end(data_chain)

            lp.move_to_next()

        return data_chain

    def post_log_reload(self, lp, view):
        if not lp.is_loop_execution:
            wx.PostEvent(view, PETPEvent(PETPEvent.LOG))

    def log_end_process(self, current_loop, loopParam, processor, task, view):
        logging.info(
            f'<-{task.end} <- {type(processor).__name__} <--------------< Task: {loopParam.get_sequence()} {(current_loop.get_loop_code() + "#" + str(loopParam.loop_times_cur)) if current_loop is not None else ""} Done \n')
        self.post_log_reload(loopParam, view)

    def log_start_process(self, current_loop, loopParam, processor, task, view):
        logging.info(
            f'>-{task.start} >- {type(processor).__name__} >---------------> Task: {loopParam.get_sequence()} {(current_loop.get_loop_code() + "#" + str(loopParam.loop_times_cur)) if current_loop is not None else ""}')
        logging.info(f'process start: {task.input}')
        self.post_log_reload(loopParam, view)

    def initTask(self, data_chain, idx, sequence) -> Task:
        task: Task = self.list[idx]
        task.data_chain = data_chain
        task.start = DateUtil.get_now_in_str("%Y-%m-%d %H:%M:%S")
        task.run_sequence = sequence
        return task

    def initiProcessor(self, task, view, current_loop, is_loop_execution, condition) -> Processor:
        processor: Processor = Processor.get_processor_by_type(task.type)
        processor.set_execution(self)
        processor.set_task(task)
        processor.set_condition(condition)
        processor.set_view(view)
        processor.set_in_loop(is_loop_execution)
        processor.set_current_loop(current_loop)
        return processor

    def find_current_loop(self, sequence) -> Loop:
        if not hasattr(self, 'loops'):
            return None

        for loop in self.loops:
            if loop.get_task_start() <= sequence <= loop.get_task_end():
                loop.verify_loop()
                return loop
            else:
                return None

    def _get_file_path(self):
        return f'{os.path.realpath(".")}{os.sep}core{os.sep}executions{os.sep}{self.execution}.yaml'

    def delete(self):
        OSUtils.copy2(self._get_file_path(), os.path.realpath('core') + f'{os.sep}executions{os.sep}trash{os.sep}')
        OSUtils.delete_file_if_existed(self._get_file_path())

    def save(self):
        if len(self.list) > 0:
            YamlRO.write(self._get_file_path(), self)
            logging.info('Successfully save execution -> ' + self._get_file_path())

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def get_execution(filename):
        file_absolute_path = f'{os.path.realpath(".")}{os.sep}core{os.sep}executions{os.sep}{filename}.yaml'
        if OSUtils.is_file_existed(file_absolute_path):
            return YamlRO.get_yaml_from_file(file_absolute_path)
        else:
            logging.warning(f'File not existed: {file_absolute_path}')
            return None

    @staticmethod
    def get_available_executions():
        executions = OSUtils.get_file_list(os.path.realpath('core') + os.sep + 'executions')
        result = list(
            map(
                lambda f: f.replace('.yaml', ''),
                filter(
                    lambda f: '.yaml' in f,
                    executions
                )
            )
        )
        result.sort()
        return result
