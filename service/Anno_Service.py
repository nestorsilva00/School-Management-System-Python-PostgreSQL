from .Establish_Connection import  Establish_conecction
from model import Anno
from model import Curso
from service import Curso_Service


class Anno_Service:
    def create_anno (self, anno, cod_curso):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_anno', (anno, cod_curso))
        cursor.close()
        con.commit()
        con.close()

    def delete_anno (self, cod_anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_anno', (cod_anno,))
        cursor.close()
        con.commit()
        con.close()

    def update_anno (self, anno , cod_curso, cod_anno):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_anno', (anno, cod_curso, cod_anno))
        cursor.close()
        con.commit()
        con.close()

    def read_anno (self):
        annos = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from anno")
        rows = cursor.fetchall()
        for r in rows:
            annos.append(Anno.Anno(r[1], r[2], r[0]))
        cursor.close()
        con.close()
        return annos


    def get_anno(self, cod_anno):
        annos = Anno_Service.read_anno(Anno_Service)
        for i in annos:
            if i.get_cod_anno() == cod_anno:
                return i.get_anno()

    def get_cod_curso(self, cod_anno):
        annos = Anno_Service.Anno_Service.read_anno(Anno_Service)
        for i in annos:
            if i.get_cod_anno() == cod_anno:
                return i.get_cod_curso(i.get_cod_anno)


    def crear_annos_nuevo_curso(self, cod_nuevo_curso, ctdad_annos):
        for i in range(ctdad_annos):
            Anno_Service.create_anno(Anno_Service, i+1, cod_nuevo_curso)


    def annos_por_curso(self, curso_cod):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('annos_por_curso', ('ref', curso_cod,))
        cursor2 = con.cursor('ref')
        rows = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        con.close()
        return rows


    def get_annos_x_curso(self, curso):
        cod_curso = Curso_Service.Curso_Service.get_cod_curso_x_curso(Curso_Service, curso)
        annos = Anno_Service.read_anno(Anno_Service)
        annos_curso = []

        for anno in annos:
            if anno.get_cod_curso() == cod_curso:
                annos_curso.append(anno)

        return annos_curso

    def get_cod_anno_por_curso(self, anno, curso_cod):
        annos = Anno_Service.read_anno(Anno_Service)
        for i in annos:
            if i.get_anno() == anno and i.get_cod_curso() == curso_cod:
                return i.get_cod_anno()