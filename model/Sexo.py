class Sexo:
    def __init__(self, cod_sexo, sexo):
        self.cod_sexo = cod_sexo
        self.sexo = sexo

    def get_cod_sexo(self): return self.cod_sexo

    def get_sexo(self): return self.sexo

    def set_cod_sexo(self, new_cod_sexo):  self.cod_sexo = new_cod_sexo

    def set_sexo(self, new_sexo):  self.sexo= new_sexo
