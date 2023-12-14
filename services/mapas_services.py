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
        print("Hola Mundo desde Flask con MVC")
        if csv_file is None:
            return jsonify({'geojson_data': 'No hay archivo'})
        if csv_file == '1':
            nombre_archivo = './csv_mapas/inmuebles24Corregido.geojson'
            with open(nombre_archivo, 'r') as file:
                geojson_data = file.read()
                geojson_data = json.loads(geojson_data)
                return jsonify(  geojson_data)
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
        elif csv_file == '8':
                    nombre_archivo = './csv_mapas/michelada_31_10_23.geojson'
                    with open('./csv_mapas/michelada_31_10_23.geojson', 'r') as file:
                        geojson_data = file.read()
                        geojson_data = json.loads(geojson_data)
                        return jsonify({'geojson_data': geojson_data})


    def matriz_distancia_tiempo(origen,destino):
        

        
        result = gmaps.distance_matrix(origen, destino, mode='driving')
        distancia = result['rows'][0]['elements'][0]['distance']['text']
        distancia_metros = result['rows'][0]['elements'][0]['distance']['value']
        tiempo_llegada = result['rows'][0]['elements'][0]['duration']['text']
        tiempo_llegada_seg = result['rows'][0]['elements'][0]['duration']['value']

        # Devolver la información como JSON
        return jsonify({'distancia': distancia, 'tiempo_llegada': tiempo_llegada , 'distancia_metros': distancia_metros, 'tiempo_llegada_seg': tiempo_llegada_seg })



