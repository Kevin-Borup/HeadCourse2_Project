from static.py.Login import CheckLogin
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash

bp = Blueprint('loginPage', __name__)

@bp.route('/Login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        error = None

        user = CheckLogin(username, password)

        if user is None:
            error = 'Incorrect username or password.'
        
        if error is None:
            return redirect(url_for('profilePage.profilePage'))

        flash(error)

    return render_template('LoginPage.html', title="Login")


def logout():
    session.pop('username', None)
    return redirect(url_for('login'))