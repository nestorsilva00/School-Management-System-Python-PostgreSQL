# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertar_contraseña.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from service.Usuario_Service import Usuario_Service

class Ui_InsertarContrasenna(object):
    def setupUi(self, CambiarContrasenna):
        self.d = CambiarContrasenna
        CambiarContrasenna.setObjectName("CambiarContrasenna")
        CambiarContrasenna.resize(410, 300)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        CambiarContrasenna.setFont(font)
        CambiarContrasenna.setStyleSheet("QPushButton{\n"
"\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(112, 112, 112);\n"
"border-right:2px solid rgb(170, 170, 170);\n"
"border-bottom:2px solid rgb(170, 170, 170);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border-right:1px solid rgb(170, 170, 170);\n"
"border-bottom:1px solid rgb(170, 170, 170)\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(79, 173, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"border-bottom:2px solid rgb(75, 75, 75);\n"
"}")
        self.frame = QtWidgets.QFrame(CambiarContrasenna)
        self.frame.setGeometry(QtCore.QRect(20, 70, 371, 161))
        self.frame.setStyleSheet("QFrame{background-color: rgb(171, 171, 171);\n"
"border-radius:12px}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(79, 173, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"border-bottom:2px solid rgb(75, 75, 75);\n"
" \n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 12, 47, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 71, 21))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(180, 120, 111, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 120, 47, 21))
        self.label_4.setObjectName("label_4")
        self.lineEditNombre = QtWidgets.QLineEdit(self.frame)
        self.lineEditNombre.setGeometry(QtCore.QRect(180, 20, 113, 22))
        self.lineEditNombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.lineEditNombre.setObjectName("lineEditNombre")
        self.lineEditApellidos_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEditApellidos_2.setGeometry(QtCore.QRect(180, 70, 113, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditApellidos_2.sizePolicy().hasHeightForWidth())
        self.lineEditApellidos_2.setSizePolicy(sizePolicy)
        self.lineEditApellidos_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.lineEditApellidos_2.setObjectName("lineEditApellidos_2")
        self.label = QtWidgets.QLabel(CambiarContrasenna)
        self.label.setGeometry(QtCore.QRect(0, 0, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(51, 103, 145);\n"
"border-radius:12px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(CambiarContrasenna)
        self.pushButton.setGeometry(QtCore.QRect(310, 252, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(CambiarContrasenna)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 252, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 21, 21);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(CambiarContrasenna)
        QtCore.QMetaObject.connectSlotsByName(CambiarContrasenna)
        self.pushButton.clicked.connect(self.on_pushButton)
        self.pushButton_2.clicked.connect(self.d.close)

    def retranslateUi(self, CambiarContrasenna):
        _translate = QtCore.QCoreApplication.translate
        CambiarContrasenna.setWindowTitle(_translate("CambiarContrasenna", "Dialog"))
        self.label_2.setText(_translate("CambiarContrasenna", "Usuario:"))
        self.label_3.setText(_translate("CambiarContrasenna", "Contraseña:"))
        self.comboBox.setItemText(0, _translate("CambiarContrasenna", "administrador"))
        self.comboBox.setItemText(1, _translate("CambiarContrasenna", "usuario"))
        self.label_4.setText(_translate("CambiarContrasenna", "Rol:"))
        self.label.setText(_translate("CambiarContrasenna", "Insertar usuarios"))
        self.pushButton.setText(_translate("CambiarContrasenna", "Insertar"))
        self.pushButton_2.setText(_translate("CambiarContrasenna", "Salir"))

    def on_pushButton(self):
        nombre = self.lineEditNombre.text()
        contra = self.lineEditApellidos_2.text()
        cod_usuario = Usuario_Service.get_cod_usuario_x_nombre(Usuario_Service, nombre)
        rol = self.comboBox.currentText()
        cod = 1
        if rol == "usuario":
            cod = 2
        if cod_usuario == None:
            if len(nombre)>4 and len(contra) > 4:
                Usuario_Service.create_usuario(Usuario_Service,nombre,contra,cod)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Usuario insertado correctamente")
                msg.setWindowTitle("Info")
                msg.exec_()
                self.d.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("El usuario y la contraseña deben ser mayor de 4 caracteres")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Ya existe un usuario con este nombre")
            msg.setWindowTitle("Info")
            msg.exec_()


