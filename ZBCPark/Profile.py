from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('profile', __name__)

@app.route('/Profile')
def profile():
    if 'username' in session:
        return render_template('Profile.html', title="Profile")
    return 'You are not logged in'