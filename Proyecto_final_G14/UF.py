from Archivo import *
from os.path import exists

#Clase para almacenar el registro del valor de la UF
class UF(Archivo):
    
    fecha = None
    valor = None
    
    def __init__(self, fecha=None, valor=None):
        #Inicio
        if fecha != None:
            self.fecha = fecha
        
        if valor != None:
            self.valor = valor
        
    def __str__(self):
        #Usado para imprimir el objeto resultante de ésta clase
        return f"Fecha: {self.fecha} Valor: {self.valor}"
    
    def get_fecha(self):
        #Retorna la fecha de la UF'
        return self.fecha
    
    def get_valor(self) -> float:
        #Retorna el valor del registro
        return self.valor
    
    def set_nombreArchivoGuardado(self, nombre):
        #Configura el nombre de archivo para guardar el registro
        super().set_nombre(nombre)
        
    def guardar(self):
        #Guarda el registro de UF
        registro = f"{self.fecha},{self.valor}"
        super().guardar(registro, 'w')
            
    def leer(self):
        #Lee el registro guardado     
        try:
            
            registro = super().leer('s')
            
            if registro == '':
                print('El registro de UF está vacío')
                exit(1)

            #SETEO DE LOS DATOS DEL OBJETO
            self.fecha, self.valor = registro.split(',')
            self.valor = float(self.valor)
        except ArchivoNoEncontradoException as e:
            print(e)
            exit(1)