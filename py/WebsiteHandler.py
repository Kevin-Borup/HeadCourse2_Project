from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
        return render_template('../pages/FrontPage.html', title="Home")

@app.route('/ParkingLotMap')
def parkingLotMap():
        return render_template('../pages/ParkingLotMap.html', title="Parking Lot")

@app.route('/Profile')
def profile():
    return render_template('../pages/Profile.html', title="Profile")

@app.route('/Login-Register')
def loginRegister():
    return render_template('../pages/Login-Register.html', title="Login-Register")


