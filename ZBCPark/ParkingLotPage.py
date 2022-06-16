from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from static.py.ParkingLot import GetSectorsData

bp = Blueprint('parkingLotPage', __name__)

sector1 = 1
sector2 = 2
sector3 = 3

@bp.route('/ParkingLot')
def parkingLotPage():
        sector1Data = GetSectorsData(sector1)
        (sector1Id, s1Total, s1AS, s1US) = sector1Data

        sector2Data = GetSectorsData(sector2)
        (sector2Id, s2Total, s2AS, s2US) = sector2Data

        sector3Data = GetSectorsData(sector3)
        (sector3Id, s3Total, s3AS, s3US) = sector3Data

        return render_template(
                'ParkingLotPage.html',
                title ="ParkingLot",
                sector1Total = s1Total,
                sector1AS = s1AS, 
                sector1US = s1US,
                sector2Total = s2Total,
                sector2AS = s2AS,
                sector2US = s2US,
                sector3Total = s3Total,
                sector3AS = s3AS,
                sector3US = s3US)
