from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('parkingLotMap', __name__)

@bp.route('/ParkingLotMap')
def parkingLotMap():
        return render_template('ParkingLotMap.html', title="Parking Lot")