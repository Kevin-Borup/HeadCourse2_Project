from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash

bp = Blueprint('loginPage', __name__)

@bp.route('/Login', methods=('GET', 'POST'))
def loginPage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        error = None

        # db = get_db()
        # user = db.execute(
        #     'SELECT * FROM user WHERE username = ?', (username,)
        # ).fetchone()

        # if user is None:
        #     error = 'Incorrect username.'
        # elif not check_password_hash(user['password'], password):
        #     error = 'Incorrect password.'
        
        # if error is None:
        #     session.clear()
        #     session['user_id'] = user[id]
        #     return redirect(url_for('profile'))

        flash(error)

    return render_template('LoginPage.html', title="Login")


def logout():
    session.pop('username', None)
    return redirect(url_for('login'))