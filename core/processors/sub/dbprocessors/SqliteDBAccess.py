import sqlite3
import logging

from core.processors.sub.dbprocessors.BaseDBAccess import BaseDBAccess


# sqlite3:
#   https://docs.python.org/3/library/sqlite3.html
# sqlite3 tool:
#   https://sqlitestudio.pl/

class SqliteDBAccess(BaseDBAccess):
    conn: sqlite3.Connection

    def connect(self, host, port, database, user, pwd):
        self.conn = sqlite3.connect(database)
        logging.info("Sqlite database: " + database)

    def execute(self, sql, param):
        if not hasattr(self, 'conn'):
            logging.info("Sqlite database is not connected, can NOT run sql: " + sql)
            return []

        cur: sqlite3.Cursor = self.conn.cursor()
        dataset = []
        try:

            if param is not None and len(param) > 0:
                cur.execute(sql, param)
            else:
                cur.execute(sql)

            if sql.startswith("update") or sql.startswith("delete") or sql.startswith("insert") \
                    or sql.startswith("UPDATE") or sql.startswith("DELETE") or sql.startswith("INSERT"):
                self.conn.commit()
                logging.info(f" {cur.rowcount} affected. - {sql}")

            for data in cur:
                dataset.append(data)

        except sqlite3.Error as err:
            logging.error(err)
        finally:
            cur.close()

        return dataset

    def disconnect(self):
        if (hasattr(self, 'conn')
                and self.conn is not None):
            self.conn.close()
