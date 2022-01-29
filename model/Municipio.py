from service import Municipio_Service


class Municipio:
    def __init__(self, cod_municipio, municipio):
        self.cod_municipio = cod_municipio
        self.municipio = municipio

    def get_cod_municipio(self): return self.cod_municipio

    def get_municipio(self): return self.municipio

    def set_cod_municipio(self, new_cod_municipio):  self.cod_municipio = new_cod_municipio

    def set_municipio(self, new_municipio):  self.municipio = new_municipio

    @staticmethod
    def get_cod_municipio_x_municipio(municipio):
        municipios = Municipio_Service.Municipio_Service.read_municipio(Municipio_Service.Municipio_Service)
        i = 0
        while municipios[i].get_municipio() != municipio and i < len(municipios):
            i += 1
        return municipios[i].get_cod_municipio()