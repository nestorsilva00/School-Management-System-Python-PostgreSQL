from service import Anno_Service
from model.Curso import Curso
class Anno:
    def __init__(self, cod_anno, cod_curso, anno):
        self.cod_anno = cod_anno
        #llave foranea
        self.cod_curso = cod_curso
        self.anno = anno

    def get_anno(self): return self.anno

    def get_cod_anno(self): return self.cod_anno

    def get_cod_curso (self): return self.cod_curso

    def set_anno(self, new_anno):  self.anno = new_anno

    def set_cod_anno(self, new_cod):  self.cod_anno = new_cod

    def set_cod_curso (self, new_cod): self.cod_curso = new_cod





