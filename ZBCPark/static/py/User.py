from static.py.dbConfig import config
import psycopg2

def GetUserData(userId):

        conn = None

        createdUser = None

        try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute('SELECT * FROM public.user_account WHERE id = {}'.format(userId))
                createdUser = cur.fetchone() # Fetches a single row from the database
                cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        conn.close()
                return createdUser

def AddUser(accName, accRole, accLicenseplate, accCardnumber):
    
        conn = None

        createdUser = None

        try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute('CALL public.createaccount(%s,%s,%s,%s)', accName, accRole, accLicenseplate, accCardnumber)
                cur.execute('SELECT * FROM public.user_account WHERE cardnumber = {}'.format(accCardnumber))
                createdUser = cur.fetchone() # Fetches a single row from the database
                cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        conn.close()
                return createdUser
