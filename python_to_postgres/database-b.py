from psycopg2 import pool


connection_pool = pool.SimpleConnectionPool(1,
                                            1,
                                            database='learning',
                                            user='postgres',
                                            password='a4600oldjob',
                                            host='localhost')


# def connect():
#    return psycopg2.connect(user='postgres', password='a4600oldjob', database='learning', host='localhost')