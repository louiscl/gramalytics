import sqlite3
import config
import helper
from analyzer import parser
from webapp import web_server


if __name__ == "__main__":
    conn = sqlite3.connect(config.DATABASE_PATH)
    cur = conn.cursor()

    my_parser = parser.Parser(cur)
    my_parser.parse_and_save_all()

    conn.commit()

    web_server.start()

    helper.execute_sql_commands(config.SQL_FILES_DIRECTORY + "/drop_tables.sql", cur)

    conn.close()