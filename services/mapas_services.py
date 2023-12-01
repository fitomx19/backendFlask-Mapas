from flask import Flask, request, jsonify
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

class MapasService:
    @staticmethod
    def obtener_mensaje():
        return "Hola Mundo desde Flask con MVC"

class MapasGeoJsonService:
    @staticmethod
    def obtener_geojson(csv_file):
        if csv_file is None:
            return jsonify({'geojson_data': 'No hay archivo'})
        if csv_file == '1':
            nombre_archivo = './csv_mapas/inmuebles24Corregido.csv'
        geojson_data = MapasGeoJsonService.convertir_csv_a_geojson(nombre_archivo)
        return jsonify({'geojson_data': geojson_data})
    
    def convertir_csv_a_geojson(csv_file):
        df = pd.read_csv(csv_file)
        geometry = [Point(xy) for xy in zip(df['longitud'], df['latitud'])]
        gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')
        geojson_data = gdf.to_crs('EPSG:4326').to_json()
        return geojson_data
