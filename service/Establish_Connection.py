from utils.Connection import Connection


class Establish_conecction:

    @staticmethod
    def get_connection(self):
        return Connection("localhost", "proyecto_bd", "postgres", "na581103").instance
