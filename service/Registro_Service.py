from .Establish_Connection import Establish_conecction
from model.Registro import Registro


class Registro_Service:
    def create_registro (self, cod_estudiante, cod_grupo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_registro', (cod_estudiante, cod_grupo))
        cursor.close()
        con.commit()
        con.close()

    def delete_registro (self, cod_estudiante):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_registro', (cod_estudiante,))
        cursor.close()
        con.commit()
        con.close()

    def update_registro (self, cod_estudiante, cod_grupo, cod_grupo_actual):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_registro', (cod_estudiante, cod_grupo, cod_grupo_actual,))
        cursor.close()
        con.commit()
        con.close()

    def read_registro (self):
        registro = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from registro")
        rows = cursor.fetchall()
        for r in rows:
            registro.append(Registro(r[1], r[0]))
        cursor.close()
        con.close()
        return registro




