import psycopg2
from psycopg2 import Error
# from psycopg2.extras import DictCursor


class Database:

    def __init__(self):
        # self.user = "user"
        self.user = "postgres"
        # self.password = "user"
        self.password = "jtdfmt77md"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.database = "project-1"

    def connect(self):
        try:
            self.connection = psycopg2.connect(user=self.user,
                                               password=self.password,
                                               host=self.host,
                                               port=self.port,
                                               database=self.database)
            # self.cursor = self.connection.cursor(cursor_factory=DictCursor)
            self.cursor = self.connection.cursor()
            # print(f'Connected to {self.database} in {self.host} as {self.user}')
        except (Exception, Error) as error:
            # print(f'An error occurred while connecting to {self.database} in {self.host} as {self.user}')
            return False

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            # print(f'Connection to {self.database} in {self.host} as {self.user} closed')
        else:
            # print(f'There are no active connections')
            return False
