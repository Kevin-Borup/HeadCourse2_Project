from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
        return render_template('FrontPage.html', title="Home")

@app.route('/ParkingLotMap')
def parkingLotMap():
        return render_template('ParkingLotMap.html', title="Parking Lot")

@app.route('/Profile')
def profile():
    return render_template('Profile.html', title="Profile")

@app.route('/LoginRegister')
def loginRegister():
    return render_template('LoginRegister.html', title="LoginRegister")


