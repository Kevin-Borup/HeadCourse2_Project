from flask import Flask, render_template, redirect, request, url_for
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=postgres user=postgres password=Kode1234!")

cur = conn.cursor()

cur.execute('SELECT name FROM public.ducks WHERE id = 69')

testData = cur.fetchone()

cur.close()
conn.close()

@app.route('/')
def home():
        return render_template('FrontPage.html', title="Home", data=testData)

@app.route('/ParkingLotMap')
def parkingLotMap():
        return render_template('ParkingLotMap.html', title="Parking Lot")

@app.route('/Profile')
def profile():
    return render_template('Profile.html', title="Profile")

@app.route('/LoginRegister')
def loginRegister():
    return render_template('LoginRegister.html', title="LoginRegister")


