from .Establish_Connection import Establish_conecction
from model.Municipio import Municipio


class Municipio_Service:
    def create_municipio (self, municipio):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_municipio', (municipio,))
        cursor.close()
        con.commit()
        con.close()

    def delete_municipio (self, cod_municipio):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_municipio', (cod_municipio,))
        cursor.close()
        con.commit()
        con.close()

    def update_municipio (self, cod_municipio, municipio):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_municipio', (cod_municipio, municipio))
        cursor.close()
        con.commit()
        con.close()

    def read_municipio (self):
        municipio = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from municipio")
        rows = cursor.fetchall()
        for r in rows:
            municipio.append(Municipio(r[0], r[1]))
        cursor.close()
        con.close()
        return municipio







