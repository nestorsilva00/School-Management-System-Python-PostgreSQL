class Rol:
    def __init__(self, cod_rol, rol):
        self.cod_rol = cod_rol
        self.rol = rol

    def get_cod_rol(self): return self.cod_rol

    def get_rol(self): return self.rol

    def set_cod_rol(self, new_cod_rol):  self.cod_rol = new_cod_rol

    def set_rol(self, new_rol):  self.rol = new_rol
