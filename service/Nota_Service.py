from .Establish_Connection import  Establish_conecction
from model.Nota import Nota


class Nota_Service:
    def create_nota (self, cod_asignatura, cod_estudiante, cod_anno, cod_evaluacion):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_nota', (cod_asignatura, cod_estudiante, cod_anno, cod_evaluacion))
        cursor.close()
        con.commit()
        con.close()

    def delete_nota (self, cod_asignatura, cod_estudiante, cod_anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_nota', (cod_asignatura, cod_estudiante, cod_anno))
        cursor.close()
        con.commit()
        con.close()

    def update_nota (self, cod_evaluacion, cod_asignatura, cod_estudiante, cod_anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_nota', (cod_evaluacion, cod_asignatura, cod_estudiante, cod_anno))
        cursor.close()
        con.commit()
        con.close()

    def read_nota (self):
        nota = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from nota")
        rows = cursor.fetchall()
        for r in rows:
            nota.append(Nota(r[0], r[1], r[2], r[3]))
        cursor.close()
        con.close()
        return nota

    def asignaturas_con_notas_por_estudiante(self, cod_estudiante):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('asignaturas_con_notas_por_estudiante', ('ref', cod_estudiante))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def promedio_acumulado_por_grupo(self, curso, anno, grupo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('promedios_acumulados_por_grupo', ('ref', curso, anno, grupo,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def promedio_anual_por_grupo(self, curso, anno, grupo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('promedio_anual_por_grupo', ('ref', curso, anno, grupo,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def escalafon_por_anno(self, curso, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('escalafon_anual', ('ref', curso, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def certificado_de_notas(self, est):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('reporte_notas_por_estudiante', ('ref',est,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def promedio_anual_por_estudiante(self, est, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('promedio_anual_por_estudiante', ('ref',est, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def estudiantes_suspensos_por_grupo(self, curso, anno, grupo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('estudiantes_suspensos_por_grupo', ('ref',curso, anno, grupo,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def aprobados_por_anno(self, curso, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('aprobados_por_anno', ('ref',curso, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def suspensos_por_anno(self, curso, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('suspensos_por_anno', ('ref',curso, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows





