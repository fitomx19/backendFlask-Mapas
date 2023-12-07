from flask import Flask, request, jsonify
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import json
class MapasService:
    @staticmethod
    def obtener_mensaje():
        return "Hola Mundo desde Flask con MVC"

class MapasGeoJsonService:
    @staticmethod
    def obtener_geojson(csv_file):
        print("Hola Mundo desde Flask con MVC")
        if csv_file is None:
            return jsonify({'geojson_data': 'No hay archivo'})
        if csv_file == '1':
            nombre_archivo = './csv_mapas/inmuebles24Corregido.csv'
        elif csv_file == '2':
            nombre_archivo = './csv_mapas/ids_ut_raw.csv'
        elif csv_file == '3':
            nombre_archivo = './csv_mapas/michelada_31_10_23.csv'
        elif csv_file == '4':
            nombre_archivo = './csv_mapas/output2.geojson'
            with open(nombre_archivo, 'r') as file:
                geojson_data = file.read()
                geojson_data = json.loads(geojson_data)
                return jsonify({'geojson_data': geojson_data})
        elif csv_file == '5':
            nombre_archivo = './csv_mapas/hamburguesas_04_12.geojson'
            with open('./csv_mapas/hamburguesas_04_12.geojson', 'r') as file:
                geojson_data = file.read()
                geojson_data = json.loads(geojson_data)
                return jsonify({'geojson_data': geojson_data})
        elif csv_file == '6':
            nombre_archivo = './csv_mapas/flan_04_12.geojson'
            with open('./csv_mapas/flan_04_12.geojson', 'r') as file:
                geojson_data = file.read()
                geojson_data = json.loads(geojson_data)
                return jsonify({'geojson_data': geojson_data})
        elif csv_file == '7':
            nombre_archivo = './csv_mapas/info_negocios_final.json'
            with open('./csv_mapas/info_negocios_final.json', 'r') as file:
                geojson_data = file.read()
                geojson_data = json.loads(geojson_data)
                return jsonify({'geojson_data': geojson_data})


        geojson_data = MapasGeoJsonService.convertir_csv_a_geojson(nombre_archivo)
        return jsonify({'geojson_data': json.loads(geojson_data)})

    @staticmethod
    def convertir_csv_a_geojson(csv_file):
        df = pd.read_csv(csv_file)
        #print(df.head(3))
        geometry = [Point(xy) for xy in zip(df['longitud'], df['latitud'])]
        gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')
        geojson_data = gdf.to_crs('EPSG:4326').to_json()
        #print(type(geojson_data))
        return geojson_data
    



""" class MapasGeoJsonService:
    @staticmethod
    def obtener_geojson(csv_file):
        print("Hola Mundo desde Flask con MVC")
        if csv_file is None:
            return jsonify({'geojson_data': 'No hay archivo'})
        if csv_file == '1':
            nombre_archivo = './csv_mapas/inmuebles24Corregido.csv'
        elif csv_file == '2':
            nombre_archivo = './csv_mapas/ids_ut_raw.csv'
        elif csv_file == '3':
            nombre_archivo = './csv_mapas/michelada_31_10_23.csv'
        elif csv_file == '4':
            nombre_archivo = './csv_mapas/output.geojson'
        else:
            return jsonify({'geojson_data': 'Archivo no válido'})

        with open(nombre_archivo, 'r') as file:
            geojson_data = file.read()
            geojson_data = json.loads(geojson_data)

        return jsonify({'geojson_data': geojson_data})

    @staticmethod
    def convertir_csv_a_geojson(csv_file):
        df = pd.read_csv(csv_file)
        
        geometry = [Point(xy) for xy in zip(df['longitud'], df['latitud'])]
        gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')
        geojson_data = gdf.to_crs('EPSG:4326').to_json()
        print(type(geojson_data))
        return geojson_data """
