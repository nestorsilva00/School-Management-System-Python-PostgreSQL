""""La tabla motivo_baja en la base de datos es una nomencladora, ya que solo contiene los
motivos de bajas y sus codigos para identificarlos"""

class Motivo_baja:
    def __init__(self, cod_motivo_baja, motivo):
        self.cod_motivo_baja = cod_motivo_baja
        self.motivo = motivo

    def get_cod_motivo_baja(self): return self.cod_motivo_baja

    def get_motivo(self): return self.motivo

    def set_cod_motivo_baja(self, new_cod_motivo_baja):  self.cod_motivo_baja = new_cod_motivo_baja

    def set_motivo(self, new_motivo):  self.motivo = new_motivo
