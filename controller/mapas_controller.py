from services.mapas_services import MapasService,MapasGeoJsonService

class MapasController:
    def saludar(self):
        mensaje = MapasService.obtener_mensaje()
        return {'mensaje': mensaje}
    
    def obtener_geojson(self, csv_file):
        geojson_data = MapasGeoJsonService.obtener_geojson(csv_file)
        return geojson_data
    
    def obtener_distancia(self,origen,destino):
        distancia = MapasGeoJsonService.matriz_distancia_tiempo(origen,destino)
        return distancia
