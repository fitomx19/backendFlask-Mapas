from flask import Flask, request, jsonify
import pandas as pd
import googlemaps
import json
class MapasService:
    @staticmethod
    def obtener_mensaje():
        return "Hola Mundo desde Flask con MVC"
google_maps_api_key = 'AIzaSyCwwLJHujEZM1HVi-D8FWKeR_gug2QrtAo'
gmaps = googlemaps.Client(key=google_maps_api_key)

class MapasGeoJsonService:
    @staticmethod
    def obtener_geojson(csv_file):
        archivos = {
            '1': './csv_mapas/inmuebles24Corregido.geojson',
            '2': './csv_mapas/ids_ut_raw.csv',
            '3': './csv_mapas/michelada_31_10_23.csv',
            '4': './csv_mapas/output2.geojson',
            '5': './csv_mapas/hamburguesas_04_12.geojson',
            '6': './csv_mapas/flan_04_12.geojson',
            '7': './csv_mapas/info_negocios_final.json',
            '8': './csv_mapas/michelada_31_10_23.geojson'
        }

        if csv_file not in archivos:
            return jsonify({'geojson_data': 'Archivo no encontrado'})
        
        nombre_archivo = archivos[csv_file]
        
        try:
            with open(nombre_archivo, 'r') as file:
                geojson_data = json.loads(file.read())
                return jsonify({'geojson_data': geojson_data})
        except Exception as e:
            return jsonify({'error': str(e)})



    def matriz_distancia_tiempo(origen,destino):
        

        
        result = gmaps.distance_matrix(origen, destino, mode='driving')
        distancia = result['rows'][0]['elements'][0]['distance']['text']
        distancia_metros = result['rows'][0]['elements'][0]['distance']['value']
        tiempo_llegada = result['rows'][0]['elements'][0]['duration']['text']
        tiempo_llegada_seg = result['rows'][0]['elements'][0]['duration']['value']

        # Devolver la información como JSON
        return jsonify({'distancia': distancia, 'tiempo_llegada': tiempo_llegada , 'distancia_metros': distancia_metros, 'tiempo_llegada_seg': tiempo_llegada_seg })



