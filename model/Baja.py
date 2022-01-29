

"""Esta tabla en la base de datos es una entidad debil ya que tiene solo dos llave foraneas
o sea, no puede definirse por si misma"""

class Baja:
    def __init__(self, cod_baja, cod_estudiante):
        self.cod_baja = cod_baja
        self.cod_estudiante = cod_estudiante

    def get_cod_baja(self): return self.cod_baja

    def get_cod_estudiante(self): return self.cod_estudiante

    def set_cod_baja(self, new_cod_baja):  self.cod_baja = new_cod_baja

    def set_cod_estudiante(self, new_cod_estudiante):  self.cod_estudiante = new_cod_estudiante
