
from PyQt5.QtWidgets import QApplication, QDialog
import sys
from view.Login.login import Ui_Autenticar
from service.Usuario_Service import Usuario_Service


if __name__ == "__main__":

        app = QApplication(sys.argv)
        login = QDialog(parent=None)
        ui = Ui_Autenticar()
        ui.setupUi(login)
        login.show()
        sys.exit(app.exec_())






