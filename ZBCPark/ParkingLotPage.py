from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from static.py.ParkingLot import AddCarToParkingLot, RemoveCarFromParkingLot

bp = Blueprint('parkingLotPage', __name__)

@bp.route('/ParkingLot')
def parkingLotPage():
        return render_template(
                'ParkingLotPage.html',
                title="Parking Lot")