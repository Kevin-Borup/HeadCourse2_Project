from static.py.dbConfig import config
import psycopg2

def CheckLoginData(email, password):
        
    conn = None

    userId = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('CALL public.checklogin(%s,%s)', email, password)
        userId = cur.fetchone() # Fetches a single row from the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        
        user = {"userId":userId}
        return user