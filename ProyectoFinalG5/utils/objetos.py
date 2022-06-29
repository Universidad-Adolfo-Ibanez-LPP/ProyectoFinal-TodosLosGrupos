#definir objeto de pelicula y sus parametros
class Pelicula:
   def __init__(self, titulo, anio, director, genero, cast, duracion, score, review):
        self.titulo = titulo
        self.anio = anio
        self.director = director
        self.genero = genero
        self.cast = cast
        self.duracion = duracion
        self.score = score
        self.review = review 

#definir objeto de conjunto y sus parametros
class Conjunto:
   def __init__(self, promedio, minimo, maximo, reviews):
      self.promedio = promedio
      self.minimo = minimo
      self.maximo = maximo
      self.reviews = reviews


class Datos:
   def __init__(self, min_largo, max_largo, min_anio, max_anio, promedio):
      self.min_largo = min_largo
      self.max_largo = max_largo
      self.min_anio = min_anio
      self.max_anio = max_anio
      self.promedio = promedio
      