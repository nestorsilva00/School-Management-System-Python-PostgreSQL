from service import Curso_Service
from service import Anno_Service
from model import Curso

class Asignatura:
    def __init__(self, cod_asignatura, hora, asignatura, cod_anno):
        self.cod_asignatura = cod_asignatura
        self.hora = hora
        self.asignatura = asignatura
        self.cod_anno = cod_anno

    def get_cod_asignatura(self): return self.cod_asignatura

    def get_hora(self): return self.hora

    def get_asignatura(self): return self.asignatura

    def get_cod_anno(self): return self.cod_anno

    def set_cod_asignatura(self, new_cod_asignatura):  self.cod_asignatura = new_cod_asignatura

    def set_hora(self, new_hora):  self.hora = new_hora

    def set_asignatura(self, new_asignatura):  self.asignatura = new_asignatura

    def set_cod_anno(self, new_cod_anno):  self.cod_asignatura = new_cod_anno

