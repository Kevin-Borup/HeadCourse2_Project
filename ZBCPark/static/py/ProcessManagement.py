from static.py.dbConfig import config
import psycopg2

def AddGateRecord(sectorId, gateTimestamp, userLicenseplate, enteredParkinglot):
        
        conn = None

        newGateRecord = None

        try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute('CALL public.addgaterecord(%s,%s,%s,%s)', sectorId, gateTimestamp, userLicenseplate, enteredParkinglot)
                cur.execute('SELECT * FROM public.gate WHERE licenseplate = {userLicenseplate}')
                newGateRecord = cur.fetchone() # Fetches a single row from the database
                cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        conn.close()
                return newGateRecord
