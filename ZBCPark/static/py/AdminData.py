from static.py.dbConfig import config
import psycopg2

def getAdminData():
            
    conn = None

    adminData = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT name FROM public.user_account')
        adminData = cur.fetchall() # Fetches all rows from the database that matches the condition
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        return adminData

def getUserData(uName):
    conn = None

    userData = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT name, licenseplate, role FROM public.user_account WHERE name = {0}'.format(uName))
        userData = cur.fetchone() # Fetches all rows from the database that matches the condition
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        return userData