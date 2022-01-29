class Usuario:

    def __init__(self, cod_usuario, usuario, password, cod_rol):
        self.cod_usuario= cod_usuario
        self.usuario = usuario
        self.password = password
        self.cod_rol = cod_rol

    def get_cod_usuario(self): return self.cod_usuario

    def get_usuario(self): return self.usuario

    def get_password(self): return self.password

    def get_cod_rol(self): return self.cod_rol

    def set_cod_usuario(self, new_cod_usuario):  self.cod_usuario = new_cod_usuario

    def set_usuario(self, new_usuario):  self.usuario = new_usuario

    def set_password(self, new_password):  self.password = new_password

    def set_cod_rol(self, new_cod_rol):  self.cod_rol = new_cod_rol




