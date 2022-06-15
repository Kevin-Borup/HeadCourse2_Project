from flask import Flask, render_template
from static.py.ParkingLot import GetSectorsData, AddCarToParkingLot, RemoveCarFromParkingLot
from static.py.User import GetUserData, AddUser
app = Flask(__name__)

sector1 = 1
sector2 = 2
sector3 = 3

@app.route('/')
async def home():

        sector1Data = GetSectorsData(sector1)
        (sector1Id, s1Total, s1AS, s1US) = sector1Data

        sector2Data = GetSectorsData(sector2)
        (sector2Id, s2Total, s2AS, s2US) = sector2Data

        sector3Data = GetSectorsData(sector3)
        (sector3Id, s3Total, s3AS, s3US) = sector3Data

        return render_template(
                'FrontPage.html',
                title ="Home",
                sector1Total = s1Total,
                sector1AS = s1AS, 
                sector1US = s1US,
                sector2Total = s2Total,
                sector2AS = s2AS,
                sector2US = s2US,
                sector3Total = s3Total,
                sector3AS = s3AS,
                sector3US = s3US)

@app.route('/ParkingLotMap')
def parkingLotMap():
        return render_template(
                'ParkingLotMap.html',
                title="Parking Lot")

@app.route('/Profile')
def profile():

        randomId = 1
        userData = GetUserData(randomId)
        (id, name, role, licenseplate, cardnumber) = userData

        return render_template(
            'Profile.html',
            title="Profile",
            userId = id,
            userName = name,
            userRole = role,
            userLicenseplate = licenseplate,
            userCardnumber = cardnumber)

@app.route('/Login')
def login():
    return render_template(
            'LoginPage.html',
            title="Login")

@app.route('/Register')
def register():
    return render_template(
            'RegisterPage.html',
            title="Register")
