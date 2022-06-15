from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('frontPage', __name__)

@bp.route('/')
def home():
        return render_template('FrontPage.html', title="Home")
