from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from static.py.User import GetUserData

bp = Blueprint('profile', __name__)

@bp.route('/Profile')
def profile():
    #if 'username' in session:
    #    return render_template('Profile.html', title="Profile")
    #return 'You are not logged in'
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