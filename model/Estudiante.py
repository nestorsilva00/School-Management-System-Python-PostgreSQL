"""Clase modelo de la tabla estudiante en la base de datos"""

from service.Municipio_Service import Municipio_Service
from service.Sexo_Service import Sexo_Service
from service import Estudiante_Service
from service.Registro_Service import Registro_Service
from service.Nota_Service import Nota_Service
from service.Grupo_Service import Grupo_Service
from service import Baja_Service



class Estudiante:
    def __init__(self, cod_estudiante, nom_estudiante, apellidos, cod_sexo, cod_municipio):
        self.cod_estudiante = cod_estudiante
        self.nom_estudiante = nom_estudiante
        self.apellidos = apellidos
        self.cod_sexo = cod_sexo
        self.cod_municipio = cod_municipio

    def get_cod_estudiante(self): return self.cod_estudiante

    def get_nom_estudiante(self): return self.nom_estudiante

    def get_apellidos(self): return self.apellidos

    def get_cod_sexo(self): return self.cod_sexo

    def get_cod_municipio(self): return self.cod_municipio

    def set_cod_estudiante(self, new_cod_estudiante):  self.cod_estudiante = new_cod_estudiante

    def set_nom_estudiante(self, new_nom_estudiante):  self.nom_estudiante = new_nom_estudiante

    def set_apellidos(self, new_apellidos):  self.apellidos = new_apellidos

    def set_cod_sexo(self, new_cod_sexo):  self.cod_sexo = new_cod_sexo

    def set_cod_municipio(self, new_cod_municipio):  self.cod_municipio = new_cod_municipio

    def get_municipio(self):
        municipios = Municipio_Service.read_municipio(Municipio_Service)
        i=0
        while municipios[i].get_cod_municipio()!=self.get_cod_municipio() and i < len(municipios):
                i+=1
        return municipios[i].get_municipio()

    def get_sexo(self):
        sexos = Sexo_Service.read_sexo(Sexo_Service)
        i = 0
        while sexos[i].get_cod_sexo() != self.get_cod_sexo() and i < len(sexos):
            i += 1
        return sexos[i].get_sexo()

    def get_grupo(self):
       return Estudiante_Service.Estudiante_Service.get_grupo_estudiante(Estudiante_Service.Estudiante_Service,self.cod_estudiante)






