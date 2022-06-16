from static.py.dbConfig import config
import psycopg2

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

def AddCarToParkingLot(sectorId):

    conn = None

    spaceOverview = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('CALL addcartoparkinglot(%s)', sectorId)
        cur.execute('SELECT * FROM public.parkinglot WHERE sector = {}'.format(sectorId))
        spaceOverview = cur.fetchone() # Fetches a single row from the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    finally:
                if conn is not None:
                        conn.close()
                return spaceOverview

def RemoveCarFromParkingLot(sectorId):

    conn = None

    spaceOverview = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('CALL removecartoparkinglot(%s)', sectorId)
        cur.execute('SELECT * FROM public.parkinglot WHERE sector = {}'.format(sectorId))
        spaceOverview = cur.fetchone() # Fetches a single row from the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    finally:
                if conn is not None:
                        conn.close()
                return spaceOverview
