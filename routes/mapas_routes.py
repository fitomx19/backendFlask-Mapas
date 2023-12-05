from flask import Blueprint,send_from_directory
from backendFlask.controller.mapas_controller import MapasController

mapas_bp = Blueprint('mapas', __name__)

@mapas_bp.route('/')
def hola_mundo():
    return MapasController().saludar()

@mapas_bp.route('/geojson/<csv_file>')
def obtener_geojson(csv_file):
    return MapasController().obtener_geojson(csv_file)

@mapas_bp.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)