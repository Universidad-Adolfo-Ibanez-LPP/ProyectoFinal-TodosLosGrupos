

class Medicamento():

    def __init__(self,medicamento ,farmacia, descripcion,precio_clp,precio_uf):
        self.medicamento = medicamento
        self.farmacia = farmacia
        self.descripcion = descripcion
        self.precio_clp = precio_clp
        self.precio_uf = precio_uf

    def __str__(self): 
        return self.medicamento + "," + self.farmacia + "," + '"' + self.descripcion.strip() + '"' + "," + str(self.precio_clp) + "," + str(self.precio_uf)
       
    
    def __repr__(self): 
        return self.medicamento + "," + self.farmacia + "," + '"' + self.descripcion.strip() + '"' + "," + str(self.precio_clp) + "," + str(self.precio_uf)

    def get_medicamento(self):
        return self.medicamento
    def get_farmacia(self):
        return self.farmacia
    def get_descripcion(self):
        return self.descripcion
    def get_precio_clp(self):
        return self.precio_clp
    def get_precio_uf(self):
        return self.precio_uf


    def a_lista(self):
        return [self.medicamento,self.farmacia,self.descripcion.strip(),self.precio_clp,self.precio_uf]
