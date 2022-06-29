import UFprice


class Producto(object):
    def __init__(self, activo, farmacia, descripcion, precioClp):
        self.__activo = activo
        self.__farmacia = farmacia
        self.__descripcion = descripcion
        self.__precioClp = float(precioClp)
        self.__precioUf = (precioClp / UFprice.getUFprice())

    @property
    def activo(self):
        return self.__activo

    @property
    def farmacia(self):
        return self.__farmacia

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precioClp(self):
        return self.__precioClp

    @property
    def precioUf(self):
        return self.__precioUf

    @activo.setter
    def activo(self, activo):
        self.__activo = activo

    @farmacia.setter
    def farmacia(self, farmacia):
        self.__farmacia = farmacia

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @precioClp.setter
    def precioClp(self, precioClp):
        self.__precioClp = precioClp

    @precioUf.setter
    def precioUf(self, precioUf):
        self.__precioUf = precioUf


medicamentos = []
