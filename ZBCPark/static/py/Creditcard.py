from static.py.dbConfig import config
import psycopg2

def AddCreditcard(userCardnumber, name, cvc, expiryDate):

        conn = None

        createdCreditcard = None

        try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute('CALL public.addcreditcard(%s,%s,%s,%s)', userCardnumber, name, cvc, expiryDate)
                cur.execute('SELECT * FROM public.creditcard WHERE cardnumber = {userCardnumber}')
                createdCreditcard = cur.fetchone() # Fetches a single row from the database
                cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        conn.close()
                return createdCreditcard