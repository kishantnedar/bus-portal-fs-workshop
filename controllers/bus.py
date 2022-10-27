from flask import Blueprint, jsonify
from actions.bus.bus import BusActions


bus = Blueprint('bus', __name__)


@bus.route('/bus/<int:bus_no>', methods=['GET'])
def get_bus(bus_no):
    bus = BusActions().get_bus(bus_no)
    return jsonify(bus)
