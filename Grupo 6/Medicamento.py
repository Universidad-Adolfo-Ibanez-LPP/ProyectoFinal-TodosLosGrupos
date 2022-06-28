

class Medicamento():

    def __init__(self,medicamento ,farmacia, descripcion,precio_clp,precio_uf):
        self.medicamento = medicamento
        self.farmacia = farmacia
        self.descripcion = descripcion
        self.precio_clp = precio_clp
        self.precio_uf = precio_uf

    def __str__(self): 
        return self.medicamento + "," + self.farmacia + "," + '"' + self.descripcion.strip() + '"' + "," + str(self.precio_clp) + "," + str(self.precio_uf)
        # return  {'farmacia':self.farmacia,'descripcion': self.descripcion,'precio_clp': self.precio_clp,'precio_uf': self.precio_uf}
    
    
    # def __repr__(self): 
    #     return self.farmacia + "," + '"',self.descripcion.trim()+'"' + "," + str(self.precio_clp) + "," + str(self.precio_uf)

    def a_lista(self):
        return [self.medicamento,self.farmacia,self.descripcion.strip(),self.precio_clp,self.precio_uf]
