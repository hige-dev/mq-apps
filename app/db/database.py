import psycopg2
from configparser import ConfigParser

class Database:
    def __init__(self, filename='db/dbconfig.ini', section='postgresql'):
        self.__config(filename, section)

    def __connect(self):
        conn = psycopg2.connect(**self.dbconf)
        conn.set_client_encoding('utf-8')
        self.__connection = conn
        self.__cursor = conn.cursor()

    def __close(self):
        self.__cursor.close()
        self.__connection.close()

    def __config(self, filename, section):
        parser = ConfigParser()
        parser.read(filename)

        self.dbconf = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                self.dbconf[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    def __execute(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__connection.commit()
        except psycopg2.Error as e:
            print(e)
            self.__connection.rollback()

    def select_all(self):
        self.__connect()
        sql = 'select * from users'
        self.__execute(sql)
        res = self.__cursor.fetchall()
        self.__close()
        return res

    def insert_user(self, name):
        self.__connect()
        sql = f'insert into users (name) values (\'{name}\')'
        self.execute(sql)
        self.__close()
