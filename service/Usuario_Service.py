from .Establish_Connection import  Establish_conecction
from model.Usuario import Usuario
from hashlib import md5

class Usuario_Service:
    def verificar_credenciales(self,nombre,contrasenna):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('verificar_credenciales', (nombre, md5(contrasenna.encode()).hexdigest()))
        var = cursor.fetchone()[0]
        return var

    def create_usuario (self, nombre, contrasenna,  cod_rol):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_usuario', (nombre, md5(contrasenna.encode()).hexdigest(),  cod_rol))
        cursor.close()
        con.commit()
        con.close()

    def delete_usuario (self, cod_usuario):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_usuario', (cod_usuario,))
        cursor.close()
        con.commit()
        con.close()

    def update_usuario (self, cod_usuario , contrasenna):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('cambiar_contrasenna', (cod_usuario, md5(contrasenna.encode()).hexdigest()))
        cursor.close()
        con.commit()
        con.close()

    def read_usuario (self):
        usuario = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from usuario")
        rows = cursor.fetchall()
        for r in rows:
            usuario.append(Usuario(r[0], r[1], r[2], r[3]))
        cursor.close()
        con.close()
        return usuario


    def get_cod_usuario_x_nombre(self,nombre):
        usuarios = self.read_usuario(self)
        for usuario in usuarios:
            if usuario.usuario == nombre:
                return usuario.cod_usuario
        return None