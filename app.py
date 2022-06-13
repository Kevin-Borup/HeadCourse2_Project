from flask import Flask, render_template
from static.py.dbConfig import config
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
        return render_template('FrontPage.html', title="Home", data=getTestName())

@app.route('/ParkingLotMap')
def parkingLotMap():
        return render_template('ParkingLotMap.html', title="Parking Lot")

@app.route('/Profile')
def profile():
    return render_template('Profile.html', title="Profile")

@app.route('/LoginRegister')
def loginRegister():
    return render_template('LoginRegister.html', title="LoginRegister")

def getTestName():
        conn = None
        testData = None
        try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute('SELECT name FROM public.user_account WHERE id = 1')
                testData = cur.fetchone() # Fetches a single row from the database
                cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        conn.close()
                return testData
