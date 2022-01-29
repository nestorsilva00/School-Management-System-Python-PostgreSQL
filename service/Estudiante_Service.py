from .Establish_Connection import Establish_conecction
from model.Estudiante import Estudiante
from service.Nota_Service import Nota_Service
from service.Baja_Service import Baja_Service
from service.Registro_Service import Registro_Service
from service.Grupo_Service import Grupo_Service
import re

class Estudiante_Service:
    def create_estudiante (self, nombre, apellidos, cod_municipio, cod_sexo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_estudiante', (nombre, apellidos, cod_municipio, cod_sexo))
        con.commit()
        cursor.close()
        con.close()

    def delete_estudiante (self, cod_estudiante):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_estudiante', (cod_estudiante,))
        con.commit()
        cursor.close()
        con.close()

    def update_estudiante (self,cod, nombre, apellidos, cod_municipio, cod_sexo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_estudiante', (cod,nombre, apellidos,  cod_municipio, cod_sexo))
        con.commit()
        cursor.close()
        con.close()

    def read_estudiante (self):
        estudiantes = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from estudiante")
        rows = cursor.fetchall()
        for r in rows:
            estudiantes.append(Estudiante(r[2], r[0], r[1], r[4], r[3]))
        cursor.close()
        con.close()
        return estudiantes

    def report_lista_estudiantes_grupo(self):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('reporte_estudiantes_por_grupo', ('ref',))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def get_grupo_estudiante(self,cod_estudiante):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('estudiante_devolver_grupo', (cod_estudiante,))
        num_grupo = cursor.fetchall()[0][0]
        cursor.close()
        con.close()
        return num_grupo

    def get_estudinates_filtrados_ambos_sexos(self,curso,anno,grupo):
        estudiantes = []
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('estudiantes_filtrados_ambos_sexos',(curso,anno,grupo,'ref',))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        for r in rows:
            string = re.sub('["/()]',"",r[0])
            strings = string.split(",")
            var = []
            var.append(Estudiante(int(strings[2]), strings[0], strings[1], int(strings[4]), int(strings[3])))
            var.append(r[1])
            estudiantes.append(var)
        cursor.close()
        cursor2.close()
        con.close()
        return estudiantes

    def get_estudinates_filtrados_un_sexo(self,curso,anno,grupo,sexo):
        estudiantes = []
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('estudiantes_filtrados_un_sexo',(curso,anno,grupo,'ref',sexo,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        for r in rows:
            string = re.sub('["/()]',"",r[0])
            strings = string.split(",")
            var = []
            var.append(Estudiante(int(strings[2]), strings[0], strings[1], int(strings[4]), int(strings[3])))
            var.append(r[1])
            estudiantes.append(var)
        cursor.close()
        cursor2.close()
        con.close()
        return estudiantes


    def get_nombre_estudiante(self, cod_estudiante):
        estudiantes = self.read_estudiante(self)
        for i in estudiantes:
            if i.get_cod_estudiante() == cod_estudiante:
                return i.get_nom_estudiante()+" "+i.get_apellidos()


    def repitentes_por_anno(self, curso, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('repitentes_por_anno', ('ref', curso, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def grupo_anno_y_curso_por_estudiante(self, cod_estudiante):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('grupo_anno_y_curso_por_estudiante', ('ref', cod_estudiante,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def get_cod_grupo_actual(self, cod_estudiante):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('cod_grupo_actual_por_estudiante', ('ref', cod_estudiante,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def llenar_grupos_con_estudiantes(self, ctdad_annos, curso_nombre, nuevo_curso):
        for i in range(ctdad_annos):
            if i == 0:
                suspensos = Nota_Service.suspensos_por_anno(Nota_Service, curso_nombre, i + 1)
                ctdad_grupos = round(len(suspensos) / 5)
                grupos=Grupo_Service.get_grupos_por_anno_y_curso2(Grupo_Service, nuevo_curso, i+1)
                cont = 0
                for j in suspensos:
                    if cont >= len(grupos):
                        cont=0
                        Registro_Service.create_registro(Registro_Service, j[0], grupos[cont][2])
                        cont+=1
                    else:
                        Registro_Service.create_registro(Registro_Service, j[0], grupos[cont][2])
                        cont += 1
            else:
                aprobados = Nota_Service.aprobados_por_anno(Nota_Service, curso_nombre, i)
                suspensos = Nota_Service.suspensos_por_anno(Nota_Service, curso_nombre, i + 1)
                total=aprobados+suspensos
                ctdad_grupos = round((len(suspensos) + len(aprobados)) / 5)
                grupos = Grupo_Service.get_grupos_por_anno_y_curso2(Grupo_Service, nuevo_curso, i +1)
                cont = 0
                for j in total:
                    if cont >= len(grupos):
                        cont = 0
                        Registro_Service.create_registro(Registro_Service, j[0], grupos[cont][2])
                        cont += 1
                    else:
                        Registro_Service.create_registro(Registro_Service, j[0], grupos[cont][2])
                        cont += 1

    def isBaja(cod_est):
        bajas = Baja_Service.read_baja(Baja_Service)
        for baja in bajas:
            if baja.get_cod_estudiante() == cod_est:
                return True
        return False