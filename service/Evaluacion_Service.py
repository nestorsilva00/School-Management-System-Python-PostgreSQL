from .Establish_Connection import  Establish_conecction
from model.Evaluacion import Evaluacion


class Evaluacion_Service:
    def create_evaluacion (self, cod_evaluacion, evaluacion):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_evaluacion', (cod_evaluacion, evaluacion))
        cursor.close()
        con.commit()
        con.close()

    def delete_evaluacion (self, cod_evaluacion):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_evaluacion', (cod_evaluacion,))
        cursor.close()
        con.commit()
        con.close()

    def update_evaluacion (self, cod_evaluacion, evaluacion):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_evaluacion', (cod_evaluacion, evaluacion))
        cursor.close()
        con.commit()
        con.close()

    def read_evaluacion (self):
        evaluacion = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from evaluacion")
        rows = cursor.fetchall()
        for r in rows:
            evaluacion.append(Evaluacion(r[0], r[1]))
        cursor.close()
        con.close()
        return evaluacion

    def report_evaluaciones_asignaturas_grupo(self):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('reporte_evaluaciones_por_grupo', ('ref',))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def get_cod_evaluacion(self, evaluacion):
        evaluaciones = self.read_evaluacion(self)
        for i in evaluaciones:
            if i.get_evaluacion()==evaluacion:
                return i.get_cod_evaluacion()


    def get_evaluacion(self, cod_evaluacion):
        evaluaciones = self.read_evaluacion(self)
        for i in evaluaciones:
            if i.get_cod_evaluacion() == cod_evaluacion:
                return i.get_evaluacion()
