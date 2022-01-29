from service import Grupo_Service
from service.Nota_Service import Nota_Service
from service.Anno_Service import Anno_Service
from service.Establish_Connection import Establish_conecction
from model.Anno import *


class Grupo:
    def __init__(self, cod_grupo, cod_anno, num_grupo):
        self.cod_grupo = cod_grupo
        self.cod_anno = cod_anno
        self.num_grupo = num_grupo

    def get_cod_grupo(self):
        return self.cod_grupo

    def get_cod_anno(self):
        return self.cod_anno

    def get_num_grupo(self):
        return self.num_grupo

    def set_cod_grupo(self, new_cod_grupo):
        self.cod_grupo = new_cod_grupo

    def set_cod_anno(self, new_cod_anno):
        self.cod_anno = new_cod_anno

    def set_num_grupo(self, new_num_grupo):
        self.num_grupo = new_num_grupo

    # El valor que devuelve es de tipo int
    @staticmethod
    def get_cod_grupo_x_num_grupo(num_grupo):
        grupos = Grupo_Service.Grupo_Service.get_grupos_ultimo_curso(Grupo_Service)
        for i in grupos:
            if i.get_num_grupo() == num_grupo:
                return i.get_cod_grupo()

    # La lista que devuelve es una listas de objetos de tipo string
    @staticmethod
    def get_numeros_grupos_ultimo_curso():
        grupo_numeros = []
        grupos = Grupo_Service.Grupo_Service.get_grupos_ultimo_curso(Grupo_Service)
        for i in grupos:
            grupo_numeros.append(i.get_num_grupo())
        return grupo_numeros


    def grupos_por_anno(self, curso_nombre, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('grupos_por_anno_y_curso', ('ref', curso_nombre, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

