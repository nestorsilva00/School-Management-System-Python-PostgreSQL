from .Establish_Connection import Establish_conecction
from model.Baja import Baja


class Baja_Service:
    def create_baja (self,  cod_estudiante,cod_baja):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_baja', (cod_estudiante, cod_baja))
        cursor.close()
        con.commit()
        con.close()

    def delete_baja (self, cod_estudiante):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_baja', (cod_estudiante,))
        cursor.close()
        con.commit()
        con.close()

    def update_baja (self, cod_baja, cod_estudiante):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_baja', (cod_baja, cod_estudiante))
        cursor.close()
        con.commit()
        con.close()

    def read_baja (self):
        bajas = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from baja")
        rows = cursor.fetchall()
        for r in rows:
            bajas.append(Baja(r[1], r[0]))
        cursor.close()
        con.close()
        return bajas

    def read_bajas_por_anno(self, curso, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('estudiantes_bajas_por_anno', ('ref', curso, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def read_bajas_por_grupo(self, curso, anno, grupo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('estudiantes_bajas_por_grupo', ('ref', curso, anno, grupo,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows





