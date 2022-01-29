
""""La tabla evaluacion en la base de datos es una nomencladora, ya que solo contiene las 
evaluaciones y sus codigos para identificarlas"""
class Evaluacion:
    def __init__(self, cod_evaluacion, evaluacion):
        self.cod_evaluacion = cod_evaluacion
        self.evaluacion = evaluacion

    def get_cod_evaluacion(self): return self.cod_evaluacion

    def get_evaluacion(self): return self.evaluacion

    def set_cod_evaluacion(self, new_cod_evaluacion):  self.cod_evaluacion = new_cod_evaluacion

    def set_evaluacion(self, new_evaluacion):  self.evaluacion = new_evaluacion
