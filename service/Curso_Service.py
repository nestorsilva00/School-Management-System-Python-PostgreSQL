from .Establish_Connection import  Establish_conecction
from model import Curso
from model import Grupo
from service  import Anno_Service
from service  import Asignatura_Service
from service  import Grupo_Service
from service  import Estudiante_Service
from model import Estudiante
from model import Asignatura


class Curso_Service:
    def create_curso (self, curso):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_curso', (curso,))
        cursor.close()
        con.commit()
        con.close()

    def delete_curso (self, cod_curso):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_curso', (cod_curso,))
        cursor.close()
        con.commit()
        con.close()

    def update_curso (self, cod_curso, curso):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_curso', (cod_curso, curso))
        cursor.close()
        con.commit()
        con.close()

    def read_curso (self):
        cursos = []
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from curso")
        rows = cursor.fetchall()
        for r in rows:
            cursos.append(Curso.Curso(r[1], r[0]))
        cursor.close()
        con.close()
        return cursos

    def get_curso(self, cod_curso):
        cursos = self.read_curso(self)
        for i in cursos:
            if i.get_cod_curso() == cod_curso:
                return i.get_curso()


    def iniciar_nuevo_curso(self, nuevo_curso, ctdad_annos):
        cursos=Curso_Service.read_curso(Curso_Service)
        curso_anterior=cursos[len(cursos)-1].get_curso()
        self.create_curso(self, nuevo_curso)
        cod_curso = Curso_Service.get_cod_curso_x_curso(Curso_Service, nuevo_curso)
        #se crean los annos
        Anno_Service.Anno_Service.crear_annos_nuevo_curso(Anno_Service, cod_curso, ctdad_annos)
        #se crean los grupos
        Grupo_Service.Grupo_Service.crear_grupos_nuevo_curso(Grupo_Service, cod_curso,ctdad_annos, curso_anterior)
        #se llenan los grupos con los estudiantes
        Estudiante_Service.Estudiante_Service.llenar_grupos_con_estudiantes(Estudiante, ctdad_annos,curso_anterior, nuevo_curso)
        #crear asignautras
        Asignatura_Service.Asignatura_Service.crear_asignaturas_nuevo_curso(Asignatura_Service, ctdad_annos)


    def get_cod_curso_x_curso(self, curso):
        cursos = Curso_Service.read_curso(Curso_Service)
        for c in cursos:
            if c.get_curso() == curso:
                return c.get_cod_curso()

    def curso_actual(self):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('curso_actual', ('ref',))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows