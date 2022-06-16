from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from static.py.User import GetUserData

bp = Blueprint('profilePage', __name__)

@bp.route('/Profile')
def profilePage():
    #if 'username' in session:
    #    return render_template('Profile.html', title="Profile")
    #return 'You are not logged in'
    randomId = 1
    userData = GetUserData(randomId)
    (id, name, role, licenseplate) = userData

    return render_template(
        'ProfilePage.html',
        title="Profile",
        userId = id,
        userName = name,
        userRole = role,
        userLicenseplate = licenseplate)