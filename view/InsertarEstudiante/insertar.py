# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox
from service.Grupo_Service import Grupo_Service
from service.Estudiante_Service import Estudiante_Service
from service.Municipio_Service import Municipio_Service
from service.Registro_Service import Registro_Service
from model.Grupo import Grupo
from model.Municipio import Municipio
from utils.Validaciones import solo_alpha_spaces


class Ui_DialogInsertarEstudiante(object):
    def setupUi(self, DialogInsertarEstudiante):
        self.d = DialogInsertarEstudiante
        DialogInsertarEstudiante.setObjectName("DialogInsertarEstudiante")
        DialogInsertarEstudiante.resize(310, 370)
        DialogInsertarEstudiante.setMinimumSize(QtCore.QSize(310, 370))
        DialogInsertarEstudiante.setMaximumSize(QtCore.QSize(310, 370))
        DialogInsertarEstudiante.setStyleSheet("\n"
"QPushButton{\n"
"\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(112, 112, 112);\n"
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
"\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(79, 173, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"border-bottom:2px solid rgb(75, 75, 75);\n"
" \n"
"}")
        self.frame = QtWidgets.QFrame(DialogInsertarEstudiante)
        self.frame.setGeometry(QtCore.QRect(10, 10, 291, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(171, 171, 171);\n"
"border-radius:12px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(51, 103, 145);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(DialogInsertarEstudiante)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 291, 251))
        self.frame_2.setStyleSheet("background-color: rgb(171, 171, 171);\n"
"border-radius:12px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditNombre = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditNombre.setGeometry(QtCore.QRect(140, 10, 113, 22))
        self.lineEditNombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.lineEditNombre.setObjectName("lineEditNombre")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(30, 210, 55, 16))
        self.label_6.setObjectName("label_6")
        self.lineEditApellidos = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditApellidos.setGeometry(QtCore.QRect(140, 60, 113, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditApellidos.sizePolicy().hasHeightForWidth())
        self.lineEditApellidos.setSizePolicy(sizePolicy)
        self.lineEditApellidos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.lineEditApellidos.setObjectName("lineEditApellidos")
        self.comboBoxGrupos = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxGrupos.setGeometry(QtCore.QRect(140, 110, 111, 22))
        self.comboBoxGrupos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.comboBoxGrupos.setObjectName("comboBoxGrupos")
        self.comboBoxMunicipio = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxMunicipio.setGeometry(QtCore.QRect(140, 160, 111, 22))
        self.comboBoxMunicipio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.comboBoxMunicipio.setObjectName("comboBoxMunicipio")
        self.comboBoxSexo = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxSexo.setGeometry(QtCore.QRect(140, 210, 111, 22))
        self.comboBoxSexo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.comboBoxSexo.setObjectName("comboBoxSexo")
        self.pushButtonInsertar = QtWidgets.QPushButton(DialogInsertarEstudiante)
        self.pushButtonInsertar.setGeometry(QtCore.QRect(240, 330, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInsertar.setFont(font)
        self.pushButtonInsertar.setStyleSheet("")
        self.pushButtonInsertar.setObjectName("pushButtonInsertar")
        self.pushButtonSalir = QtWidgets.QPushButton(DialogInsertarEstudiante)
        self.pushButtonSalir.setGeometry(QtCore.QRect(10, 330, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSalir.setFont(font)
        self.pushButtonSalir.setStyleSheet("background-color: rgb(255, 21, 21);")
        self.pushButtonSalir.setObjectName("pushButtonSalir")
        self.pushButtonInsertarContinuar = QtWidgets.QPushButton(DialogInsertarEstudiante)
        self.pushButtonInsertarContinuar.setGeometry(QtCore.QRect(90, 330, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInsertarContinuar.setFont(font)
        self.pushButtonInsertarContinuar.setObjectName("pushButtonInsertarContinuar")

        self.retranslateUi(DialogInsertarEstudiante)
        QtCore.QMetaObject.connectSlotsByName(DialogInsertarEstudiante)
        DialogInsertarEstudiante.setTabOrder(self.lineEditNombre, self.lineEditApellidos)
        DialogInsertarEstudiante.setTabOrder(self.lineEditApellidos, self.comboBoxGrupos)
        DialogInsertarEstudiante.setTabOrder(self.comboBoxGrupos, self.comboBoxMunicipio)
        DialogInsertarEstudiante.setTabOrder(self.comboBoxMunicipio, self.comboBoxSexo)
        DialogInsertarEstudiante.setTabOrder(self.comboBoxSexo, self.pushButtonInsertar)
        DialogInsertarEstudiante.setTabOrder(self.pushButtonInsertar, self.pushButtonSalir)
        #----------------
        self.pushButtonInsertar.clicked.connect(self.on_pushButtonInsertar_clicked)
        self.pushButtonSalir.clicked.connect(self.d.close)
        self.pushButtonInsertarContinuar.clicked.connect(self.on_pushButtonInsertarContinuar_clicked)
        self.llenar_combobox()

    def retranslateUi(self, DialogInsertarEstudiante):
        _translate = QtCore.QCoreApplication.translate
        DialogInsertarEstudiante.setWindowTitle(_translate("DialogInsertarEstudiante", "Insertar"))
        self.label.setText(_translate("DialogInsertarEstudiante", "Datos estudiantes"))
        self.label_2.setText(_translate("DialogInsertarEstudiante", "Nombre:"))
        self.label_3.setText(_translate("DialogInsertarEstudiante", "Apellidos:"))
        self.label_4.setText(_translate("DialogInsertarEstudiante", "Grupo:"))
        self.label_5.setText(_translate("DialogInsertarEstudiante", "Municipio:"))
        self.label_6.setText(_translate("DialogInsertarEstudiante", "Sexo:"))
        self.pushButtonInsertar.setText(_translate("DialogInsertarEstudiante", "Insertar"))
        self.pushButtonSalir.setText(_translate("DialogInsertarEstudiante", "Salir"))
        self.pushButtonInsertarContinuar.setText(_translate("DialogInsertarEstudiante", "Insertar y Continuar"))

    def on_pushButtonInsertarContinuar_clicked(self):
        nombre = self.lineEditNombre.text()
        apellidos = self.lineEditApellidos.text()
        grupo = self.comboBoxGrupos.currentText()
        municipio = self.comboBoxMunicipio.currentText()
        sexo = self.comboBoxSexo.currentText()
        if(solo_alpha_spaces(nombre) and solo_alpha_spaces(apellidos)):
            cod_sexo = 2
            if sexo=="Masculino":
                cod_sexo = 1
            Estudiante_Service.create_estudiante(Estudiante_Service,nombre,apellidos,Municipio.get_cod_municipio_x_municipio(municipio),cod_sexo)
            lista = Estudiante_Service.read_estudiante(Estudiante_Service)
            cod = lista[len(lista)-1].get_cod_estudiante()
            cod_grupo = Grupo.get_cod_grupo_x_num_grupo(int(grupo))
            Registro_Service.create_registro(Registro_Service,cod,cod_grupo)
            self.lineEditNombre.setText("")
            self.lineEditApellidos.setText("")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Estudiante insertado correctamente")
            msg.setWindowTitle("Información")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Nombre o apellidos incorrectos")
            msg.setWindowTitle("Error")
            msg.exec_()


    def on_pushButtonInsertar_clicked(self):
        self.on_pushButtonInsertarContinuar_clicked()
        self.d.close()

    def llenar_combobox(self):
        grupos= Grupo_Service.get_grupos_ultimo_curso(Grupo_Service)
        for i in grupos:
            self.comboBoxGrupos.addItem(str(i.get_num_grupo()))
        muni = Municipio_Service.read_municipio(Municipio_Service)
        for i in muni:
            self.comboBoxMunicipio.addItem(str(i.get_municipio()))
        self.comboBoxSexo.addItem("Masculino")
        self.comboBoxSexo.addItem("Femenino")