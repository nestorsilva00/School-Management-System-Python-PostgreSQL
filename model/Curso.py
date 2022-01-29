from service import Curso_Service
class Curso:
    def __init__(self, cod_curso, curso):
        self.cod_curso = cod_curso

        #Este atributo sera una cadena de caracteres
        self.curso = curso

    def get_cod_curso(self): return self.cod_curso

    def get_curso(self): return self.curso

    def set_cod_curso(self, new_cod_curso):  self.cod_curso = new_cod_curso

    def set_curso(self, new_curso):  self.curso = new_curso



