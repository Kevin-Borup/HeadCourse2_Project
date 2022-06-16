from static.py.AdminData import getAdminData
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint("administratorPage", __name__)

@bp.route("/administrator")
def administratorPage():
    return render_template(
        "AdministratorPage.html",
        adminData = getAdminData())

