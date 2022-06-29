from os.path import exists

class ArchivoException(Exception):
    def __init__(self, mensajeError):
        #Inicializa el objeto que hereda del objecto Exception
        self.msg = f"ERROR {mensajeError}"
        
    def __repr__(self):
        #Representación del objeto como string, para cuando se imprime.
        return self.msg


class ArchivoRegistroVacioException(ArchivoException):
    # Indicar registros vacíos durante el desarrollo
    pass


class ArchivoNoEncontradoException(ArchivoException):
    # Indicar que un archivo no es accesible durante el desarrollo
    pass


class ArchivoModoLecturaInvalidoException(ArchivoException):
    # Indicar que el modo de lectura es invalido
    pass

class Archivo:
    # leer y escribir archivos
    nombre = None
            
    def __str__(self):
        # Imprime el objeto mostrando el nombre del archivo donde se guardan los registro
        return f"{self.__class__}: {self.nombre}"
    
    @classmethod
    def set_nombre(cls, nombre):
        #Configura la propiedad nombre
        cls.nombre = nombre
    
    @classmethod
    def get_nombre(cls):
        #Retorna la propiedad nombre
        return cls.nombre
    
    @classmethod
    def guardar(cls, registro, modoGuardado='a'):
        #Guarda un registro en el archivo designado

        if registro == '':
            raise ArchivoRegistroVacioException('El registro a guardar no puede estar vacío!')
        
        if not modoGuardado in ['a', 'w']:
            raise ArchivoException('Los modos de guardado son a y w solamente')
        
        with open(cls.nombre, modoGuardado) as archivo:
            registro = f"{registro}\n"
            archivo.write(registro)

    @classmethod
    def leer(cls, modoLectura='l'):
        #Lee los registros del archivo

        if not modoLectura in ['l', 's']:
            raise ArchivoModoLecturaInvalidoException('Los modos de lectura son l y s solamente')
        
        if not exists(cls.nombre):
            raise ArchivoNoEncontradoException(f"El archivo '{cls.nombre}' no se encuentra")
        
        with open(cls.nombre, 'r') as archivo:
            if modoLectura == 'l':
                return [linea.replace('\n', '') for linea in archivo.readlines()]
            elif modoLectura == 's':
                return archivo.readline()
            else:
                return None