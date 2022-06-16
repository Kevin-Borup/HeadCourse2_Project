from static.py.dbConfig import config
import psycopg2

class User:
    __name = None
    __licensePlate = None
    __role = None
    __creditcard = None
    
    def __init__(self, name, licensePlate, role, creditcard):
        self.__name = name
        self.__licensePlate = licensePlate
        self.__role = role
        self.__creditcard = creditcard

async def AddUser(accName, accRole, accLicenseplate, accCardnumber):
    
        conn = None

        createdUser = None

        try:
                params = await config()
                conn = await psycopg2.connect(**params)
                cur = await conn.cursor()
                await cur.execute('CALL public.createaccount(%s,%s,%s,%s)', accName, accRole, accLicenseplate, accCardnumber)
                await cur.execute('SELECT * FROM public.user_account WHERE cardnumber = {}'.format(accCardnumber))
                createdUser = await cur.fetchone() # Fetches a single row from the database
                await cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        await conn.close()
                return createdUser

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