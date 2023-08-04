import psycopg2
from configparser import ConfigParser

class Database:
    def __init__(self, filename='db/dbconfig.ini', section='postgresql'):
        self.dbconf = self.__config(filename, section)

    def __connect(self):
        conn = None
        try:
            conn = psycopg2.connect(**self.dbconf)
            conn.set_client_encoding('utf-8')
            return conn
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        return conn

    def __config(self, filename, section):
        parser = ConfigParser()
        parser.read(filename)

        dbconf = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                dbconf[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return dbconf

    def execute(self, sql):
        conn = self.__connect()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            res = cur.fetchall()
        except psycopg2.Error as e:
            print(e)
            conn.rollback()
        cur.close()
        conn.close()
        return res
