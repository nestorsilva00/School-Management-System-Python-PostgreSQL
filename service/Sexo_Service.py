from .Establish_Connection import Establish_conecction
from model.Sexo import Sexo


class Sexo_Service:
    def create_sexo (self, sexo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_sexo', (sexo,))
        cursor.close()
        con.commit()
        con.close()

    def delete_sexo (self, cod_sexo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_sexo', (cod_sexo,))
        cursor.close()
        con.commit()
        con.close()

    def update_sexo (self, cod_sexo, sexo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_sexo', (cod_sexo, sexo))
        cursor.close()
        con.commit()
        con.close()

    def read_sexo (self):
        sexo = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from sexo")
        rows = cursor.fetchall()
        for r in rows:
            sexo.append(Sexo(r[0], r[1]))
        cursor.close()
        con.close()
        return sexo





