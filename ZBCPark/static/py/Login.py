from static.py.dbConfig import config
import psycopg2

def CreateUserAndLoginAttachCreditcard(userName, userLicenseplate, userCardnumber, cardholderName, cvc, expiryDate, userEmail, userPassword):

        conn = None

        createdLogin = None

        defaultRole = "Student"

        try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute('CALL createaccount(%s,%s,%s,%s)', userName, defaultRole, userLicenseplate, userCardnumber)
                cur.execute('CALL addcreditcard(%s,%s,%s,%s)', userCardnumber, cardholderName, cvc, expiryDate)
                cur.execute('SELECT id FROM public.user_account WHERE email = {}'.format(userEmail))
                userId = cur.fetchone() # Fetches a single row from the database
                cur.execute('CALL createlogin(%s,%s,%s)', userEmail, userPassword, userId)
                cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        conn.close()
                return createdLogin

def CheckLogin(userEmail, userPassword):

        conn = None

        createdLogin = None

        try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute('CALL public.checklogin(%s,%s)', userEmail, userPassword)
                createdLogin = cur.fetchone() # Fetches a single row from the database
                cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        conn.close()
                return createdLogin