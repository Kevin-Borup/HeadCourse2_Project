from flask import (
    Blueprint, render_template
)
from static.py.User import GetUserData

bp = Blueprint('profilePage', __name__)

@bp.route('/Profile')
def profilePage():
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