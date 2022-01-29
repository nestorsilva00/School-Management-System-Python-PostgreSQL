from .Establish_Connection import  Establish_conecction
from model import Grupo
from service.Nota_Service import Nota_Service
from service.Anno_Service import Anno_Service



class Grupo_Service:
    def create_grupo (self, num_grupo, cod_anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_grupo', (num_grupo, cod_anno))
        cursor.close()
        con.commit()
        con.close()

    def delete_grupo (self, cod_grupo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_grupo', (cod_grupo,))
        cursor.close()
        con.commit()
        con.close()

    def update_grupo (self, cod_grupo, num_grupo, cod_anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_grupo', (cod_grupo, num_grupo, cod_anno))
        cursor.close()
        con.commit()
        con.close()

    def read_grupo (self):
        grupos = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from grupo")
        rows = cursor.fetchall()
        for r in rows:
            grupos.append(Grupo.Grupo(r[2], r[1], r[0]))
        cursor.close()
        con.close()
        return grupos

    # EL método get_grupos_ultimo_curso devuelve una lista con los grupos del curso actual
    # La lista que devuelve es una listas de objetos de tipo Grupo
    def get_grupos_ultimo_curso(self):
        grupos=[]
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('grupo_service_devolver_grupos_ultimo_curso', ('ref',))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        for i in rows:
            grupos.append(Grupo.Grupo(i[0], i[2], i[1]))
        cursor.close()
        cursor2.close()
        con.close()
        return grupos



    def crear_grupos_nuevo_curso(self, cod_nuevo_curso, ctdad_annos, curso_nombre):
        for i in range(ctdad_annos):
            if i == 0:
                suspensos = Nota_Service.suspensos_por_anno(Nota_Service, curso_nombre, i + 1)
                ctdad_grupos = round(len(suspensos) / 5)
                for j in range(ctdad_grupos):
                    numero_grupo = str(i + 1) + str(j + 1)
                    cod_anno = Anno_Service.get_cod_anno_por_curso(Anno_Service, i + 1, cod_nuevo_curso)
                    Grupo_Service.create_grupo(Grupo_Service, numero_grupo, cod_anno)
            else:
                aprobados = Nota_Service.aprobados_por_anno(Nota_Service, curso_nombre, i)
                suspensos = Nota_Service.suspensos_por_anno(Nota_Service, curso_nombre, i + 1)
                ctdad_grupos = round((len(suspensos) + len(aprobados)) / 5)
                for j in range(ctdad_grupos):
                    numero_grupo = str(i+1) + str(j + 1)
                    cod_anno = Anno_Service.get_cod_anno_por_curso(Anno_Service, i+1, cod_nuevo_curso)
                    Grupo_Service.create_grupo(Grupo_Service, numero_grupo, cod_anno)

    def get_grupos_por_anno_y_curso(self, curso, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('grupos_por_anno_y_curso', ('ref',curso, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def get_grupos_por_anno_y_curso2(self, curso, anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('grupos_por_anno_y_curso2', ('ref',curso, anno,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows

    def isAsignacionesGrupo(self, cod_grupo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('is_asignaciones_grupo', (cod_grupo, 'ref',))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        if len(rows) == 0:
            return False
        else:
            return True


