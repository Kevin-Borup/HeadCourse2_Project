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

async def AddCarToParkingLot(sectorId):

    conn = None

    spaceOverview = None

    try:
        params = await config()
        conn = await psycopg2.connect(**params)
        cur = await conn.cursor()
        await cur.execute('CALL addcartoparkinglot(%s)', sectorId)
        await cur.execute('SELECT * FROM public.parkinglot WHERE sector = {}'.format(sectorId))
        spaceOverview = await cur.fetchone() # Fetches a single row from the database
        await cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    finally:
                if conn is not None:
                        await conn.close()
                return spaceOverview

async def RemoveCarFromParkingLot(sectorId):

    conn = None

    spaceOverview = None

    try:
        params = await config()
        conn = await psycopg2.connect(**params)
        cur = await conn.cursor()
        await cur.execute('CALL removecartoparkinglot(%s)', sectorId)
        await cur.execute('SELECT * FROM public.parkinglot WHERE sector = {}'.format(sectorId))
        spaceOverview = await cur.fetchone() # Fetches a single row from the database
        await cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    finally:
                if conn is not None:
                        await conn.close()
                return spaceOverview

def GetSectorsData(sectorId):
        
    conn = None

    sectorData = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT * FROM public.parkinglot WHERE sector = {}'.format(sectorId))
        sectorData = cur.fetchone() # Fetches a single row from the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        return sectorData