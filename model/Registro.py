class Registro:
    def __init__(self, cod_grupo, cod_estudiante):
        self.cod_grupo = cod_grupo
        self.cod_estudiante = cod_estudiante

    def get_cod_grupo(self): return self.cod_grupo

    def get_cod_estudiante(self): return self.cod_estudiante

    def set_cod_grupo(self, new_cod_grupo):  self.cod_grupo = new_cod_grupo

    def set_cod_estudiante(self, new_cod_estudiante):  self.cod_estudiante = new_cod_estudiante
