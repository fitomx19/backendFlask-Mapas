from flask import Blueprint
from backendFlask.controller.mapas_controller import MapasController

mapas_bp = Blueprint('mapas', __name__)

@mapas_bp.route('/')
def hola_mundo():
    return MapasController().saludar()

@mapas_bp.route('/geojson/<csv_file>')
def obtener_geojson(csv_file):
    return MapasController().obtener_geojson(csv_file)
