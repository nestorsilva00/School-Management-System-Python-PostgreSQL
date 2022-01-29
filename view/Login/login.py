# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QWidget,QMessageBox
from service.Usuario_Service import Usuario_Service
from view.MenuPrincipal.DialogPrincipal import Ui_DialogPrincipal
from view.MenuPrincipal.MenuUsuario import Ui_DialogMenuUsuario





class Ui_Autenticar(object):
    def setupUi(self, Autenticar):
        self.d = Autenticar
        Autenticar.setObjectName("Autenticar")
        Autenticar.resize(735, 409)
        Autenticar.setMinimumSize(QtCore.QSize(735, 409))
        Autenticar.setMaximumSize(QtCore.QSize(735, 409))
        self.frameLogin = QtWidgets.QFrame(Autenticar)
        self.frameLogin.setEnabled(True)
        self.frameLogin.setGeometry(QtCore.QRect(0, 0, 281, 431))
        self.frameLogin.setMinimumSize(QtCore.QSize(241, 141))
        self.frameLogin.setMaximumSize(QtCore.QSize(1000, 10000))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 172, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 172, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 172, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 172, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 172, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 172, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 172, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 172, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 172, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frameLogin.setPalette(palette)
        self.frameLogin.setMouseTracking(False)
        self.frameLogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameLogin.setAutoFillBackground(False)
        self.frameLogin.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 172, 29);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(79, 173, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"border-bottom:2px solid rgb(75, 75, 75);\n"
" \n"
"}")
        self.frameLogin.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameLogin.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameLogin.setObjectName("frameLogin")
        self.labelUsuario = QtWidgets.QLabel(self.frameLogin)
        self.labelUsuario.setGeometry(QtCore.QRect(10, 190, 71, 61))
        self.labelUsuario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelUsuario.setText("")
        self.labelUsuario.setPixmap(QtGui.QPixmap(":/prefijoNuevo/User_96px.png"))
        self.labelUsuario.setScaledContents(True)
        self.labelUsuario.setObjectName("labelUsuario")
        self.label = QtWidgets.QLabel(self.frameLogin)
        self.label.setGeometry(QtCore.QRect(80, 40, 131, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/prefijoNuevo/usuario.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.labelContrasenna = QtWidgets.QLabel(self.frameLogin)
        self.labelContrasenna.setGeometry(QtCore.QRect(10, 270, 71, 51))
        self.labelContrasenna.setText("")
        self.labelContrasenna.setPixmap(QtGui.QPixmap(":/prefijoNuevo/contraseña.png"))
        self.labelContrasenna.setScaledContents(True)
        self.labelContrasenna.setObjectName("labelContrasenna")
        self.lineEditContrasenna = QtWidgets.QLineEdit(self.frameLogin)
        self.lineEditContrasenna.setGeometry(QtCore.QRect(90, 280, 151, 31))
        self.lineEditContrasenna.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEditContrasenna.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.lineEditContrasenna.setObjectName("lineEditContrasenna")
        self.lineEditUsuario = QtWidgets.QLineEdit(self.frameLogin)
        self.lineEditUsuario.setGeometry(QtCore.QRect(90, 210, 151, 31))
        self.lineEditUsuario.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEditUsuario.setStyleSheet("\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.lineEditUsuario.setObjectName("lineEditUsuario")
        self.pushButton = QtWidgets.QPushButton(self.frameLogin)
        self.pushButton.setGeometry(QtCore.QRect(110, 353, 101, 31))
        self.pushButton.setMinimumSize(QtCore.QSize(101, 31))
        self.pushButton.setMaximumSize(QtCore.QSize(101, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(94, 180, 255);\n"
"border-radius:12px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border: 4px solid transparent; \n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Autenticar)
        self.label_4.setGeometry(QtCore.QRect(280, 0, 461, 451))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/prefijoNuevo/31388.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Autenticar)
        QtCore.QMetaObject.connectSlotsByName(Autenticar)
        Autenticar.setTabOrder(self.lineEditUsuario, self.lineEditContrasenna)
        Autenticar.setTabOrder(self.lineEditContrasenna, self.pushButton)
        self.pushButton.clicked.connect(self.Autenticar_clicked)

    def retranslateUi(self, Autenticar):
        _translate = QtCore.QCoreApplication.translate
        Autenticar.setWindowTitle(_translate("Autenticar", "Autenticar"))
        self.pushButton.setText(_translate("Autenticar", "Autenticar"))

    def Autenticar_clicked(self):
        try:
            nombre = self.lineEditUsuario.text()
            contrasenna = self.lineEditContrasenna.text()
            var = Usuario_Service.verificar_credenciales(Usuario_Service,nombre,contrasenna)
            if(var == "administrador"):
                Dialog = QtWidgets.QDialog()
                pri = Ui_DialogPrincipal()
                pri.setupUi(Dialog)
                self.d.close()
                Dialog.exec()
            elif (var == "usuario"):
                Dialog = QtWidgets.QDialog()
                pri = Ui_DialogMenuUsuario()
                pri.setupUi(Dialog)
                self.d.close()
                Dialog.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Datos Incorectos")
                msg.setWindowTitle("Error")
                msg.exec()
        except Exception as r:
            print(type(r))
            print(r.args)
