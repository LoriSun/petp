#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Sun Oct  2 23:09:08 2022
#

import wx

# begin wxGlade: dependencies
import wx.adv
import wx.grid
import wx.propgrid
# end wxGlade

# begin wxGlade: extracode
import os
import wx.adv
from wx._adv import TBI_DOCK
# end wxGlade


class PETPView(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PETPView.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1400, 800))
        self.SetTitle("PET-P")

        self.statusbar = self.CreateStatusBar(2, wx.STB_ELLIPSIZE_START)
        self.statusbar.SetStatusWidths([-1, 0])
        # statusbar fields
        statusbar_fields = ["Wonderful day today!", "Laughing cures everything!"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)

        self.mainPanel = wx.Panel(self, wx.ID_ANY)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.splitterWindow = wx.SplitterWindow(self.mainPanel, wx.ID_ANY, style=wx.CLIP_CHILDREN | wx.SP_3D | wx.SP_NOBORDER)
        self.splitterWindow.SetMinimumPaneSize(100)
        mainSizer.Add(self.splitterWindow, 1, wx.EXPAND, 0)

        self.topPanel = wx.Panel(self.splitterWindow, wx.ID_ANY)

        tpSizer = wx.BoxSizer(wx.VERTICAL)

        self.notebook = wx.Notebook(self.topPanel, wx.ID_ANY)
        tpSizer.Add(self.notebook, 1, wx.EXPAND, 0)

        self.nbFirstPage = wx.Panel(self.notebook, wx.ID_ANY, style=wx.BORDER_NONE | wx.TAB_TRAVERSAL)
        self.notebook.AddPage(self.nbFirstPage, "Executions")

        nbfpSizer = wx.BoxSizer(wx.VERTICAL)

        actionPanelTopSizer = wx.BoxSizer(wx.HORIZONTAL)
        nbfpSizer.Add(actionPanelTopSizer, 0, wx.ALL | wx.EXPAND, 0)

        actionPanelTopSizer.Add((3, 30), 0, 0, 0)

        self.addRow4E = wx.Button(self.nbFirstPage, wx.ID_ANY, "+")
        self.addRow4E.SetMinSize((30, 28))
        self.addRow4E.SetToolTip("Add new row")
        actionPanelTopSizer.Add(self.addRow4E, 0, 0, 0)

        actionPanelTopSizer.Add((10, 30), 0, 0, 0)

        self.delRow4E = wx.Button(self.nbFirstPage, wx.ID_ANY, "-")
        self.delRow4E.SetMinSize((30, 28))
        self.delRow4E.SetToolTip("delete selected row(s)")
        actionPanelTopSizer.Add(self.delRow4E, 0, 0, 0)

        actionPanelTopSizer.Add((30, 30), 0, 0, 0)

        self.selectRecording = wx.Button(self.nbFirstPage, wx.ID_ANY, "Select recording")
        self.selectRecording.SetMinSize((120, 28))
        self.selectRecording.SetToolTip("Select the recording file which generated by Selenium IDE.")
        actionPanelTopSizer.Add(self.selectRecording, 0, 0, 0)

        actionPanelTopSizer.Add((10, 30), 0, 0, 0)

        self.testChooser = wx.ComboBox(self.nbFirstPage, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.testChooser.SetMinSize((120, -1))
        self.testChooser.SetToolTip("Select one test from given recording")
        actionPanelTopSizer.Add(self.testChooser, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        actionPanelTopSizer.Add((10, 30), 0, 0, 0)

        self.loadRecording = wx.Button(self.nbFirstPage, wx.ID_ANY, "Convert")
        self.loadRecording.SetMinSize((120, 28))
        self.loadRecording.SetToolTip("Convert recording into PETP Task(s)")
        actionPanelTopSizer.Add(self.loadRecording, 0, 0, 0)

        actionPanelTopSizer.Add((10, 30), 0, 0, 0)

        self.recordingLocation = wx.StaticText(self.nbFirstPage, wx.ID_ANY, "")
        actionPanelTopSizer.Add(self.recordingLocation, 0, wx.ALL, 5)

        self.splitterLR4E = wx.SplitterWindow(self.nbFirstPage, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.splitterLR4E.SetMinimumPaneSize(200)
        nbfpSizer.Add(self.splitterLR4E, 1, wx.EXPAND, 0)

        self.taskGrid = wx.grid.Grid(self.splitterLR4E, wx.ID_ANY, size=(1, 1))
        self.taskGrid.CreateGrid(3, 2)
        self.taskGrid.EnableDragGridSize(0)
        self.taskGrid.SetColLabelValue(0, "Task Chooser")
        self.taskGrid.SetColSize(0, 200)
        self.taskGrid.SetColLabelValue(1, "Input")
        self.taskGrid.SetColSize(1, 500)

        self.pgPanel = wx.Panel(self.splitterLR4E, wx.ID_ANY)

        pgSizer = wx.BoxSizer(wx.VERTICAL)

        self.topTaskPropery_bottomLoopPropery = wx.SplitterWindow(self.pgPanel, wx.ID_ANY)
        self.topTaskPropery_bottomLoopPropery.SetMinimumPaneSize(20)
        pgSizer.Add(self.topTaskPropery_bottomLoopPropery, 1, wx.EXPAND, 0)

        self.tp_topPanel = wx.Panel(self.topTaskPropery_bottomLoopPropery, wx.ID_ANY, style=wx.BORDER_THEME)

        tp_topPanelSizer = wx.BoxSizer(wx.VERTICAL)

        self.taskProperty = wx.propgrid.PropertyGridManager(self.tp_topPanel, wx.ID_ANY, style=wx.propgrid.PG_BOLD_MODIFIED | wx.propgrid.PG_HIDE_MARGIN | wx.propgrid.PG_NO_INTERNAL_BORDER)
        tp_topPanelSizer.Add(self.taskProperty, 1, wx.EXPAND, 0)

        self.pgaPanel = wx.Panel(self.tp_topPanel, wx.ID_ANY, style=wx.BORDER_NONE)
        self.pgaPanel.SetMinSize((-1, 30))
        tp_topPanelSizer.Add(self.pgaPanel, 0, wx.BOTTOM | wx.EXPAND, 0)

        pgaSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.avaibleProperties = wx.ComboBox(self.pgaPanel, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.avaibleProperties.SetMinSize((120, -1))
        self.avaibleProperties.SetToolTip("Available Properties")
        pgaSizer.Add(self.avaibleProperties, 0, wx.ALL, 2)

        pga_innder = wx.BoxSizer(wx.HORIZONTAL)
        pgaSizer.Add(pga_innder, 1, wx.EXPAND, 0)

        pga_innder.Add((10, 30), 0, 0, 0)

        self.addProperty = wx.Button(self.pgaPanel, wx.ID_ANY, "+")
        self.addProperty.SetMinSize((30, 28))
        self.addProperty.SetToolTip("Add propery")
        pga_innder.Add(self.addProperty, 0, 0, 0)

        pga_innder.Add((10, 30), 0, 0, 0)

        self.delProperty = wx.Button(self.pgaPanel, wx.ID_ANY, "-")
        self.delProperty.SetMinSize((30, 28))
        self.delProperty.SetToolTip("delete selected property")
        pga_innder.Add(self.delProperty, 0, 0, 0)

        self.datepicker = wx.adv.DatePickerCtrl(self.pgaPanel, wx.ID_ANY, style=wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        self.datepicker.SetToolTip("Fill date to selected property")
        pgaSizer.Add(self.datepicker, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        pgaSizer.Add((10, 30), 0, 0, 0)

        self.convertDDir = wx.Button(self.pgaPanel, wx.ID_ANY, "DDir")
        self.convertDDir.SetMinSize((40, 28))
        self.convertDDir.SetToolTip("get download dir ")
        pgaSizer.Add(self.convertDDir, 0, 0, 0)

        pgaSizer.Add((10, 30), 0, 0, 0)

        self.convertPWD = wx.Button(self.pgaPanel, wx.ID_ANY, "E/D")
        self.convertPWD.SetMinSize((40, 28))
        self.convertPWD.SetToolTip("Prevent to save password into files")
        pgaSizer.Add(self.convertPWD, 0, 0, 0)

        pgaSizer.Add((5, 30), 0, 0, 0)

        self.convertGetData = wx.Button(self.pgaPanel, wx.ID_ANY, "D")
        self.convertGetData.SetMinSize((40, 28))
        self.convertGetData.SetToolTip("{self.get_data(\"\")}")
        pgaSizer.Add(self.convertGetData, 0, 0, 0)

        pgaSizer.Add((5, 30), 0, 0, 0)

        self.convertGetDeepData = wx.Button(self.pgaPanel, wx.ID_ANY, "DD")
        self.convertGetDeepData.SetMinSize((40, 28))
        self.convertGetDeepData.SetToolTip("{self.get_deep_data([\"\",\"\"])}")
        pgaSizer.Add(self.convertGetDeepData, 0, 0, 0)

        self.tp_bottomPanel = wx.Panel(self.topTaskPropery_bottomLoopPropery, wx.ID_ANY, style=wx.BORDER_THEME)

        tp_bottomPanelSizer = wx.BoxSizer(wx.VERTICAL)

        self.loopProperty = wx.propgrid.PropertyGridManager(self.tp_bottomPanel, wx.ID_ANY, style=wx.propgrid.PG_BOLD_MODIFIED | wx.propgrid.PG_HIDE_MARGIN | wx.propgrid.PG_NO_INTERNAL_BORDER)
        tp_bottomPanelSizer.Add(self.loopProperty, 2, wx.EXPAND, 0)

        self.pgbPanel = wx.Panel(self.tp_bottomPanel, wx.ID_ANY, style=wx.BORDER_NONE)
        self.pgbPanel.SetMinSize((-1, 30))
        tp_bottomPanelSizer.Add(self.pgbPanel, 0, wx.BOTTOM | wx.EXPAND, 0)

        pgbSizer = wx.BoxSizer(wx.HORIZONTAL)

        pgb_innder = wx.BoxSizer(wx.HORIZONTAL)
        pgbSizer.Add(pgb_innder, 1, wx.EXPAND, 0)

        pgb_innder.Add((10, 30), 0, 0, 0)

        self.addLoop = wx.Button(self.pgbPanel, wx.ID_ANY, "+")
        self.addLoop.SetMinSize((30, 28))
        self.addLoop.SetToolTip("Add propery")
        pgb_innder.Add(self.addLoop, 0, 0, 0)

        pgb_innder.Add((10, 30), 0, 0, 0)

        self.delLoop = wx.Button(self.pgbPanel, wx.ID_ANY, "-")
        self.delLoop.SetMinSize((30, 28))
        self.delLoop.SetToolTip("delete selected property")
        pgb_innder.Add(self.delLoop, 0, 0, 0)

        pgbSizer.Add((5, 30), 0, 0, 0)

        self.convertGetData4Loop = wx.Button(self.pgbPanel, wx.ID_ANY, "D")
        self.convertGetData4Loop.SetMinSize((40, 28))
        self.convertGetData4Loop.SetToolTip("{self.get_data(\"\")}")
        pgbSizer.Add(self.convertGetData4Loop, 0, 0, 0)

        pgbSizer.Add((5, 30), 0, 0, 0)

        self.convertGetDeepData4Loop = wx.Button(self.pgbPanel, wx.ID_ANY, "DD")
        self.convertGetDeepData4Loop.SetMinSize((40, 28))
        self.convertGetDeepData4Loop.SetToolTip("{self.get_deep_data([\"\",\"\"])}")
        pgbSizer.Add(self.convertGetDeepData4Loop, 0, 0, 0)

        actionPanelSizer_e = wx.BoxSizer(wx.HORIZONTAL)
        nbfpSizer.Add(actionPanelSizer_e, 0, wx.EXPAND, 0)

        self.delExection = wx.Button(self.nbFirstPage, wx.ID_ANY, "Delete")
        self.delExection.SetMinSize((75, 28))
        self.delExection.SetToolTip("Delete selected Execution")
        actionPanelSizer_e.Add(self.delExection, 0, 0, 0)

        actionPanelSizer_e.Add((5, 30), 0, 0, 0)

        self.executionChooser = wx.ComboBox(self.nbFirstPage, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.executionChooser.SetMinSize((300, -1))
        actionPanelSizer_e.Add(self.executionChooser, 0, wx.ALL, 0)

        actionPanelSizer_e.Add((5, 30), 0, 0, 0)

        self.saveExection = wx.Button(self.nbFirstPage, wx.ID_ANY, "Save")
        self.saveExection.SetMinSize((75, 28))
        self.saveExection.SetToolTip("Save or Update selected Execution")
        actionPanelSizer_e.Add(self.saveExection, 0, 0, 0)

        actionPanelSizer_e.Add((5, 30), 0, 0, 0)

        self.runExection = wx.Button(self.nbFirstPage, wx.ID_ANY, "Run Execution")
        self.runExection.SetMinSize((200, 28))
        actionPanelSizer_e.Add(self.runExection, 0, 0, 0)

        self.nbSecondPage = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.nbSecondPage, "Pipelines")

        nbspSizer = wx.BoxSizer(wx.VERTICAL)

        piplineActionPanelTopSizer = wx.BoxSizer(wx.HORIZONTAL)
        nbspSizer.Add(piplineActionPanelTopSizer, 0, wx.ALL, 0)

        piplineActionPanelTopSizer.Add((3, 30), 0, 0, 0)

        self.addRow4P = wx.Button(self.nbSecondPage, wx.ID_ANY, "+")
        self.addRow4P.SetMinSize((30, 28))
        self.addRow4P.SetToolTip("Add row")
        piplineActionPanelTopSizer.Add(self.addRow4P, 0, 0, 0)

        piplineActionPanelTopSizer.Add((10, 30), 0, 0, 0)

        self.delRow4P = wx.Button(self.nbSecondPage, wx.ID_ANY, "-")
        self.delRow4P.SetMinSize((30, 28))
        self.delRow4P.SetToolTip("Delete selected row(s)")
        piplineActionPanelTopSizer.Add(self.delRow4P, 0, 0, 0)

        self.executionGrid = wx.grid.Grid(self.nbSecondPage, wx.ID_ANY, size=(1, 1))
        self.executionGrid.CreateGrid(8, 2)
        self.executionGrid.SetColLabelValue(0, "Execution Chooser")
        self.executionGrid.SetColSize(0, 400)
        self.executionGrid.SetColLabelValue(1, "Input")
        self.executionGrid.SetColSize(1, 800)
        nbspSizer.Add(self.executionGrid, 1, wx.EXPAND, 0)

        actionPanelSizer_p = wx.BoxSizer(wx.HORIZONTAL)
        nbspSizer.Add(actionPanelSizer_p, 0, wx.EXPAND | wx.FIXED_MINSIZE, 0)

        self.delPipeline = wx.Button(self.nbSecondPage, wx.ID_ANY, "Delete")
        self.delPipeline.SetMinSize((75, 28))
        self.delPipeline.SetToolTip("Delete selected Pipeline")
        actionPanelSizer_p.Add(self.delPipeline, 0, 0, 0)

        actionPanelSizer_p.Add((5, 30), 0, 0, 0)

        self.pipelineChooser = wx.ComboBox(self.nbSecondPage, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.pipelineChooser.SetMinSize((300, -1))
        actionPanelSizer_p.Add(self.pipelineChooser, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        actionPanelSizer_p.Add((5, 30), 0, 0, 0)

        self.savePipeline = wx.Button(self.nbSecondPage, wx.ID_ANY, "Save")
        self.savePipeline.SetMinSize((75, 28))
        self.savePipeline.SetToolTip("Save or Update selected Pipeline")
        actionPanelSizer_p.Add(self.savePipeline, 0, 0, 0)

        actionPanelSizer_p.Add((5, 30), 0, 0, 0)

        self.runPipeline = wx.Button(self.nbSecondPage, wx.ID_ANY, "Run Pipepine")
        self.runPipeline.SetMinSize((200, 28))
        actionPanelSizer_p.Add(self.runPipeline, 0, 0, 0)

        actionPanelSizer_p.Add((5, 30), 0, 0, 0)

        self.asCronChecbox = wx.CheckBox(self.nbSecondPage, wx.ID_ANY, "as cron", style=wx.ALIGN_RIGHT | wx.CHK_2STATE)
        actionPanelSizer_p.Add(self.asCronChecbox, 0, wx.ALL | wx.EXPAND, 0)

        actionPanelSizer_p.Add((5, 30), 0, 0, 0)

        self.cronInput = wx.TextCtrl(self.nbSecondPage, wx.ID_ANY, "0 * * * *", style=wx.TE_CENTRE)
        self.cronInput.SetMinSize((100, -1))
        self.cronInput.Enable(False)
        actionPanelSizer_p.Add(self.cronInput, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        actionPanelSizer_p.Add((5, 30), 0, 0, 0)

        self.lableCronExplain = wx.StaticText(self.nbSecondPage, wx.ID_ANY, "", style=wx.ALIGN_LEFT)
        self.lableCronExplain.SetMinSize((300, -1))
        actionPanelSizer_p.Add(self.lableCronExplain, 0, wx.ALL, 5)

        actionPanelSizer_p.Add((5, 30), 0, 0, 0)

        self.stopCurrentCron = wx.Button(self.nbSecondPage, wx.ID_ANY, "Stop")
        self.stopCurrentCron.SetMinSize((100, 28))
        self.stopCurrentCron.SetToolTip("Stop selected Pipeline which is running as cron")
        actionPanelSizer_p.Add(self.stopCurrentCron, 0, 0, 0)

        actionPanelSizer_p.Add((5, 30), 0, 0, 0)

        self.stopAll = wx.Button(self.nbSecondPage, wx.ID_ANY, "Stop All")
        self.stopAll.SetMinSize((100, 28))
        self.stopAll.SetToolTip("Stop all pipelines running as cron.")
        actionPanelSizer_p.Add(self.stopAll, 0, 0, 0)

        self.bottomPanel = wx.Panel(self.splitterWindow, wx.ID_ANY)

        bpvSizer = wx.BoxSizer(wx.VERTICAL)

        self.logContents = wx.TextCtrl(self.bottomPanel, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_DONTWRAP | wx.TE_LEFT | wx.TE_MULTILINE | wx.TE_READONLY)
        self.logContents.SetBackgroundColour(wx.Colour(78, 78, 78))
        self.logContents.SetForegroundColour(wx.Colour(0, 255, 0))
        bpvSizer.Add(self.logContents, 1, wx.ALL | wx.EXPAND | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 0)

        actionPanelBottomSizer = wx.FlexGridSizer(1, 3, 0, 0)
        bpvSizer.Add(actionPanelBottomSizer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.FIXED_MINSIZE, 5)

        self.reloadLog = wx.Button(self.bottomPanel, wx.ID_ANY, "Reload")
        self.reloadLog.SetMinSize((80, 28))
        actionPanelBottomSizer.Add(self.reloadLog, 0, 0, 0)

        actionPanelBottomSizer.Add((10, 30), 0, 0, 0)

        self.cleanLog = wx.Button(self.bottomPanel, wx.ID_ANY, "Clean")
        self.cleanLog.SetMinSize((80, 28))
        actionPanelBottomSizer.Add(self.cleanLog, 0, 0, 0)

        self.bottomPanel.SetSizer(bpvSizer)

        self.nbSecondPage.SetSizer(nbspSizer)

        self.pgbPanel.SetSizer(pgbSizer)

        self.tp_bottomPanel.SetSizer(tp_bottomPanelSizer)

        self.pgaPanel.SetSizer(pgaSizer)

        self.tp_topPanel.SetSizer(tp_topPanelSizer)

        self.topTaskPropery_bottomLoopPropery.SplitHorizontally(self.tp_topPanel, self.tp_bottomPanel, 180)

        self.pgPanel.SetSizer(pgSizer)

        self.splitterLR4E.SplitVertically(self.taskGrid, self.pgPanel, 730)

        self.nbFirstPage.SetSizer(nbfpSizer)

        self.topPanel.SetSizer(tpSizer)

        self.splitterWindow.SplitHorizontally(self.topPanel, self.bottomPanel, 380)

        self.mainPanel.SetSizer(mainSizer)

        self.Layout()
        self.Centre()
        _icon = wx.NullIcon
        _logo_path = os.path.realpath('image') + "/petp.png"
        _icon.CopyFromBitmap(wx.Bitmap(_logo_path , wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        _tbiIcon = wx.adv.TaskBarIcon(iconType=TBI_DOCK)
        _tbiIcon.frame=self
        _tbiIcon.SetIcon(_icon, "PETP")

        self.tbicon = _tbiIcon

        # end wxGlade

# end of class PETPView

class PETP(wx.App):
    def OnInit(self):
        self.PETP = PETPView(None, wx.ID_ANY, "")
        self.SetTopWindow(self.PETP)
        self.PETP.Show()
        return True

# end of class PETP

if __name__ == "__main__":
    PETP = PETP(0)
    PETP.MainLoop()
