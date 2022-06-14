from static.py.dbConfig import config
import psycopg2

async def CreateLogin(userEmail, userPassword, userId):

        conn = None

        createdLogin = None

        try:
                params = await config()
                conn = await psycopg2.connect(**params)
                cur = await conn.cursor()
                await cur.execute('CALL createlogin(%s,%s,%s,%s)', userEmail, userPassword, userId)
                await cur.execute('SELECT * FROM public.user_account WHERE email = {userEmail}')
                createdLogin = await cur.fetchone() # Fetches a single row from the database
                await cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        await conn.close()
                return createdLogin