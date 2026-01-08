import psycopg2

def execute_sql(query):
    
    if not query.lower().startswith("select"):
        raise Exception('only SELECT queries are allowed')
    
    try:
        conn=psycopg2.connect(
            dbname='company',
            user='postgres',
            password='password',
            host='localhost',
            port="5432"
        )

        cur=conn.cursor()
        cur.execute(query)

        rows=cur.fetchall()
        columns=[col[0] for col in cur.description]

        print(f"DB Execute - Columns: {columns}")
        print(f"DB Execute - Rows: {rows}")
        print(f"DB Execute - Row count: {len(rows)}")

        return columns, rows
    
    except Exception as e:
        print(f"Database error: {e}")
        raise
    
    finally:
        # Close cursor and connection in finally block
        if cur:
            cur.close()
        if conn:
            conn.close()
    

#que="SELECT name FROM employees;"
#execute_sql(que)
