from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1,
                                            1,
                                            database='learning',
                                            user='postgres',
                                            password='a4600oldjob',
                                            host='localhost')


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)


