from static.py.dbConfig import config
import psycopg2

class ParkingLot:
    __totalspaces = None
    __availableSpaces = None
    __usedSpaces = None

    def __init__(self, totalSpaces, availableSpaces, usedSpaces):
        self.__totalspaces = totalSpaces
        self.__availableSpaces = availableSpaces
        self.__usedSpaces = usedSpaces

    async def UpdateAmountOfParkingSpaces(sectorId, usedSpaces, availableSpaces):

        conn = None

        spaceOverview = None

        try:
                params = await config()
                conn = await psycopg2.connect(**params)
                cur = await conn.cursor()
                await cur.execute('CALL updateparkinglot(%s,%s,%s)', sectorId, usedSpaces, availableSpaces)
                await cur.execute('SELECT * FROM public.parkinglot WHERE sector = {sectorId}')
                spaceOverview = await cur.fetchone() # Fetches a single row from the database
                await cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        await conn.close()
                return spaceOverview
        
    async def GetAvailableSpaces(sectorId):

        conn = None

        availableSpaces = None

        try:
                params = await config()
                conn = await psycopg2.connect(**params)
                cur = await conn.cursor()
                await cur.execute('SELECT availablespaces FROM public.parkinglot WHERE sector = {sectorId}')
                availableSpaces = await cur.fetchone() # Fetches a single row from the database
                await cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        await conn.close()
                return availableSpaces
        
    async def GetUsedSpaces():
        
        conn = None

        usedSpaces = None

        try:
                params = await config()
                conn = await psycopg2.connect(**params)
                cur = await conn.cursor()
                await cur.execute('SELECT usedspaces FROM public.parkinglot WHERE sector = {sectorId}')
                usedSpaces = await cur.fetchone() # Fetches a single row from the database
                await cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        await conn.close()
                return usedSpaces