from Archivo import *
from os.path import getsize

class Resultado(Archivo):
    '''Almacena el registro de un resultado de búsqueda de principios activos'''
    principioActivo = None
    farmacia = None
    descripcion = None
    # CLP SIN DECIMALES
    precioFinal = None
    # UF CON 2 DECIMALES
    precioUF = None
    
    def set_nombreArchivoGuardado(self, nombre):
        '''Configura el nombre de archivo para guardar el registro'''
        super().set_nombre(nombre)
        
    def set_principioActivo(self, nombre):
        '''Configura el principio activo del resultado'''
        self.principioActivo = nombre
        
    def set_farmacia(self, nombre):
        '''Configura el nombre de la farmacia del resultado'''
        self.farmacia = nombre
        
    def set_descripcion(self, texto):
        '''Configura el texto de la descripción del resultado'''
        self.descripcion = texto
        
    def set_precioFinal(self, precio):
        '''Configura el precio final del resultado'''
        self.precioFinal = precio
        
    def set_precioUF(self, precio):
        '''Configura el precio UF del resultado'''
        self.precioUF = precio
        
    def guardar(self):
        '''Guarda el registro en el archivo destinado para tal propósito'''
        registro = f"{self.principioActivo},{self.farmacia},{self.precioFinal},{self.precioUF},\"{self.descripcion}\""

        # USO LA CLASE ARCHIVO PARA GUARDAR EL REGISTRO
        super().guardar(registro, 'a')