from static.py.dbConfig import config
import psycopg2

class ProcessManagement:
    __parkinglots = None

    def __init__(self, parkinglots):
        self.__parkinglots = parkinglots

async def AddGateRecord(sectorId, gateTimestamp, userLicenseplate, enteredParkinglot):
        
        conn = None

        newGateRecord = None

        try:
                params = await config()
                conn = await psycopg2.connect(**params)
                cur = await conn.cursor()
                await cur.execute('CALL public.addgaterecord(%s,%s,%s,%s)', sectorId, gateTimestamp, userLicenseplate, enteredParkinglot)
                await cur.execute('SELECT * FROM public.gate WHERE licenseplate = {userLicenseplate}')
                newGateRecord = await cur.fetchone() # Fetches a single row from the database
                await cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        await conn.close()
                return newGateRecord
