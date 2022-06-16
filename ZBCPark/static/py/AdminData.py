from static.py.dbConfig import config
import psycopg2

def getAdminData():
            
    conn = None

    adminData = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT name, licenseplate FROM public.user_account')
        adminData = cur.fetchone() # Fetches a single row from the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        return adminData