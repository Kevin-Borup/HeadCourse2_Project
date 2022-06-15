from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from static.py.ParkingLot import AddCarToParkingLot, RemoveCarFromParkingLot

bp = Blueprint('parkingLotMap', __name__)



@bp.route('/ParkingLotMap')
def parkingLotMap():
        return render_template(
                'ParkingLotMap.html',
                title="Parking Lot")