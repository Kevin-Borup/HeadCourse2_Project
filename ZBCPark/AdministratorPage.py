from static.py.AdminData import getAdminData, getUserData
from flask import (
    Blueprint, render_template, request, jsonify
)

bp = Blueprint("administratorPage", __name__)

@bp.route("/administrator", methods = ['GET', 'POST'])
def administratorPage():
    if (request.method == 'POST'):
        return

    return render_template(
        "AdministratorPage.html",
        adminData = getAdminData())

@bp.route("/GetUser", methods = ['POST'])
def GetUserPost():
    if (request.method == 'POST'):
        uName = request.form['userName']

        userData = getUserData(uName)
        if userData is not None:
            (name, licenseplate, role) = userData
            return jsonify({'name': name, 'licenseplate': licenseplate, 'role': role})

        return jsonify({'error': 'No user data'})


