from turtle import title
from flask import (
    Blueprint, flash, render_template, request
)
bp = Blueprint('registerPage', __name__)

@bp.route('/Register')
def registerPage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        flash(error)

    return render_template('RegisterPage.html', title='Register')