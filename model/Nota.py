class Nota:
    def __init__(self, cod_asignatura, cod_estudiante, cod_anno, cod_evaluacion):
        self.cod_asignatura = cod_asignatura
        self.cod_estudiante = cod_estudiante
        self.cod_anno = cod_anno
        self.cod_evaluacion = cod_evaluacion

    def get_cod_asignatura(self): return self.cod_asignatura

    def get_cod_anno(self): return self.cod_anno

    def get_cod_estudiante(self): return self.cod_estudiante

    def get_cod_evaluacion(self): return self.cod_evaluacion

    def set_cod_asignatura(self, new_cod_asignatura):  self.cod_asignatura = new_cod_asignatura

    def set_cod_anno(self, new_cod_anno):  self.nota= new_cod_anno

    def set_cod_estudiante(self, new_cod_estudiante):  self.cod_estudiante = new_cod_estudiante

    def set_cod_evaluacion(self, new_cod_evaluacion):  self.cod_evaluacion = new_cod_evaluacion
