import psycopg2

def get_connection():
    return psycopg2.connect(

        dbname='company',
        user='postgres',
        password='password',
        host='localhost',
        port='5432'
    )


