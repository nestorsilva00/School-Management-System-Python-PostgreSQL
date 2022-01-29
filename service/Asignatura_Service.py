from service.Establish_Connection import Establish_conecction
from model import Asignatura
from service import Curso_Service
from service import Anno_Service


class Asignatura_Service:
    def create_asignatura (self, nombre, horas,  cod_anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_asignatura', (nombre, horas,  cod_anno))
        cursor.close()
        con.commit()
        con.close

    def delete_asignatura (self, cod_asignatura):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_asignatura', (cod_asignatura,))
        cursor.close()
        con.commit()
        con.close()

    def update_asignatura (self, cod_asig, nombre , horas, cod_anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_asignatura', (cod_asig, nombre , horas, cod_anno))
        cursor.close()
        con.commit()
        con.close()

    def read_asignatura (self):
        asignaturas = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from asignatura")
        rows = cursor.fetchall()
        for r in rows:
            asignaturas.append(Asignatura.Asignatura(r[3], r[1], r[0],r[2]))
        cursor.close()
        con.close()
        return asignaturas

    def read_asignatura_por_estudiante (self, est):
        asignaturas = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('asignaturas_por_estudiante_2', ('ref', est,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        for r in rows:
            asignaturas.append(Asignatura.Asignatura(r[0], r[2], r[1], r[3]))
        cursor.close()
        con.close()
        return asignaturas

    def report_lista_asignaturas_anno(self):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('reporte_asignaturas_impartidas', ('ref',))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows


    def crear_asignaturas_nuevo_curso(self, ctdad_annos):
        cursos= Curso_Service.Curso_Service.read_curso(Curso_Service)
        for i in range(ctdad_annos):
            cod_anno=Anno_Service.Anno_Service.get_cod_anno_por_curso(Anno_Service, i+1, cursos[len(cursos)-1].get_cod_curso())
            asignaturas_por_anno= Asignatura_Service.get_asignaturas_por_anno(self, cursos[len(cursos)-2].get_curso(), i+1)
            for j in asignaturas_por_anno:
                Asignatura_Service.create_asignatura(self, j[0], j[1], cod_anno)


    def asignaturas_por_estudiante(self, cod_estudiante):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('asignaturas_por_estudiante', ('ref',cod_estudiante,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def get_cod_asignatura(self, asignatura_nombre, est_cod):
        asignaturas = self.read_asignatura_por_estudiante(self, est_cod)
        for i in asignaturas:
            if i.get_asignatura()==asignatura_nombre:
                return i.get_cod_asignatura()

    def get_cod_anno(self, cod_asignatura):
        asignaturas = self.read_asignatura(self)
        for i in asignaturas:
            if i.get_cod_asignatura()==cod_asignatura:
                return i.get_cod_anno()

    def get_asignatura_nombre(self, cod_asignatura):
        asignaturas = self.read_asignatura(self)
        for i in asignaturas:
            if i.get_cod_asignatura() == cod_asignatura:
               return i.get_asignatura()

    def get_asignaturas_por_anno(self, curso, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('asignaturas_por_anno', ('ref',curso, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def get_asignatura_por_codAsignatura(self, cod_asignatura):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('asignatura_por_cod_asignatura', ('ref', cod_asignatura,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def codigo_asignaturas_con_nota(self):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('codigo_de_asignaturas_con_nota', ('ref',))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows