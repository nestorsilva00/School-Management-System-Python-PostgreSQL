from .Establish_Connection import Establish_conecction
from model.Rol import Rol


class Rol_Service:
    def create_rol (self, rol):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_rol', (rol,))
        cursor.close()
        con.commit()
        con.close()

    def delete_rol (self, cod_rol):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_rol', (cod_rol,))
        cursor.close()
        con.commit()
        con.close()

    def update_rol (self, cod_rol, rol):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_rol', (cod_rol, rol))
        cursor.close()
        con.commit()
        con.close()

    def read_rol (self):
        rol = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from rol")
        rows = cursor.fetchall()
        for r in rows:
            rol.append(Rol(r[0], r[1]))
        cursor.close()
        con.close()
        return rol





