from .Establish_Connection import Establish_conecction
from model.Motivo_Baja import Motivo_baja


class Motivo_Baja_Service:
    def create_motivo_baja (self, motivo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('create_motivo_baja', (motivo,))
        cursor.close()
        con.commit()
        con.close()

    def delete_motivo_baja (self, cod_motivo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('delete_motivo_baja', (cod_motivo,))
        cursor.close()
        con.commit()
        con.close()

    def update_motivo_baja (self, cod_motivo, motivo):
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.callproc('update_motivo_baja', (cod_motivo, motivo))
        cursor.close()
        con.commit()
        con.close()

    def read_motivo_baja (self):
        motivos = list()
        con = Establish_conecction.get_connection(Establish_conecction)
        cursor = con.cursor()
        cursor.execute("select* from motivo_baja")
        rows = cursor.fetchall()
        for r in rows:
            motivos.append(Motivo_baja(r[1], r[0]))
        cursor.close()
        con.close()
        return motivos

    def get_codMotivo_dado_motivo(self, motivo):
        motivos = Motivo_Baja_Service.read_motivo_baja(Motivo_Baja_Service)
        for i in motivos:
            if i.get_motivo()==motivo:
                return i.cod_motivo_baja
