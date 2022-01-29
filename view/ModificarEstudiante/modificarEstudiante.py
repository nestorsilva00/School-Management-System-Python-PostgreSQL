# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarEstudiante.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from service.Registro_Service import Registro_Service
from service.Grupo_Service import Grupo_Service
from service.Estudiante_Service import Estudiante_Service
from service.Municipio_Service import Municipio_Service
from model.Municipio import Municipio
from model.Grupo import Grupo


class Ui_DialogModificarEstudiante(object):
    def setupUi(self, DialogModificarEstudiante,est):
        self.d = DialogModificarEstudiante
        self.estudiante = est
        DialogModificarEstudiante.setObjectName("DialogModificarEstudiante")
        DialogModificarEstudiante.resize(310, 370)
        DialogModificarEstudiante.setMinimumSize(QtCore.QSize(310, 370))
        DialogModificarEstudiante.setMaximumSize(QtCore.QSize(310, 370))
        DialogModificarEstudiante.setStyleSheet("\n"
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
        self.frame = QtWidgets.QFrame(DialogModificarEstudiante)
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
        self.frame_2 = QtWidgets.QFrame(DialogModificarEstudiante)
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
        self.pushButtonSalir = QtWidgets.QPushButton(DialogModificarEstudiante)
        self.pushButtonSalir.setGeometry(QtCore.QRect(10, 330, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSalir.setFont(font)
        self.pushButtonSalir.setStyleSheet("background-color: rgb(255, 21, 21);")
        self.pushButtonSalir.setObjectName("pushButtonSalir")
        self.pushButtonInsertar = QtWidgets.QPushButton(DialogModificarEstudiante)
        self.pushButtonInsertar.setGeometry(QtCore.QRect(220, 330, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInsertar.setFont(font)
        self.pushButtonInsertar.setStyleSheet("")
        self.pushButtonInsertar.setObjectName("pushButtonInsertar")

        self.retranslateUi(DialogModificarEstudiante)
        QtCore.QMetaObject.connectSlotsByName(DialogModificarEstudiante)
        DialogModificarEstudiante.setTabOrder(self.lineEditNombre, self.lineEditApellidos)
        DialogModificarEstudiante.setTabOrder(self.lineEditApellidos, self.comboBoxGrupos)
        DialogModificarEstudiante.setTabOrder(self.comboBoxGrupos, self.comboBoxMunicipio)
        DialogModificarEstudiante.setTabOrder(self.comboBoxMunicipio, self.comboBoxSexo)
        DialogModificarEstudiante.setTabOrder(self.comboBoxSexo, self.pushButtonInsertar)
        DialogModificarEstudiante.setTabOrder(self.pushButtonInsertar, self.pushButtonSalir)
        #------------------
        self.llenar_combobox()
        self.lineEditNombre.setText(self.estudiante.get_nom_estudiante())
        self.lineEditApellidos.setText(self.estudiante.get_apellidos())
        self.pushButtonInsertar.clicked.connect(self.on_pushButtonModificar_clicked)
        self.pushButtonSalir.clicked.connect(self.d.close)


    def retranslateUi(self, DialogModificarEstudiante):
        _translate = QtCore.QCoreApplication.translate
        DialogModificarEstudiante.setWindowTitle(_translate("DialogModificarEstudiante", "Dialog"))
        self.label.setText(_translate("DialogModificarEstudiante", "Datos estudiantes"))
        self.label_2.setText(_translate("DialogModificarEstudiante", "Nombre:"))
        self.label_3.setText(_translate("DialogModificarEstudiante", "Apellidos:"))
        self.label_4.setText(_translate("DialogModificarEstudiante", "Grupo:"))
        self.label_5.setText(_translate("DialogModificarEstudiante", "Municipio:"))
        self.label_6.setText(_translate("DialogModificarEstudiante", "Sexo:"))
        self.pushButtonSalir.setText(_translate("DialogModificarEstudiante", "Salir"))
        self.pushButtonInsertar.setText(_translate("DialogModificarEstudiante", "Modificar"))

    def on_pushButtonModificar_clicked(self):
            nombre = self.lineEditNombre.text()
            apellidos = self.lineEditApellidos.text()
            grupo = self.comboBoxGrupos.currentText()
            municipio = self.comboBoxMunicipio.currentText()
            sexo = self.comboBoxSexo.currentText()
            cod_sexo = 2
            if sexo=="Masculino":
                    cod_sexo = 1
            Estudiante_Service.update_estudiante(Estudiante_Service,self.estudiante.get_cod_estudiante(), nombre, apellidos,Municipio.get_cod_municipio_x_municipio(municipio),cod_sexo)
            cod_grupo_actual = Estudiante_Service.get_cod_grupo_actual(Estudiante_Service, self.estudiante.get_cod_estudiante())[0][1]
            cod_grupo = Grupo.get_cod_grupo_x_num_grupo(int(grupo))
            Registro_Service.update_registro(Registro_Service,self.estudiante.get_cod_estudiante(),cod_grupo, cod_grupo_actual)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Estudiante modificado correctamente")
            msg.setWindowTitle("Información")
            msg.exec_()
            self.d.close()

    def llenar_combobox(self):
            anno_actual = Estudiante_Service.grupo_anno_y_curso_por_estudiante(Estudiante_Service, self.estudiante.get_cod_estudiante())[0][1]
            curso_actual = Estudiante_Service.grupo_anno_y_curso_por_estudiante(Estudiante_Service,self.estudiante.get_cod_estudiante())[0][2]
            grupos= Grupo.grupos_por_anno(Grupo, curso_actual, anno_actual)
            for i in grupos:
               self.comboBoxGrupos.addItem(str(i[0]))
            muni = Municipio_Service.read_municipio(Municipio_Service)
            for i in muni:
               self.comboBoxMunicipio.addItem(str(i.get_municipio()))
            self.comboBoxSexo.addItem("Masculino")
            self.comboBoxSexo.addItem("Femenino")
            self.comboBoxMunicipio.setCurrentText(self.estudiante.get_cod_municipio())# dentro de cod_municipio y get_cod_sexo
            self.comboBoxSexo.setCurrentText(self.estudiante.get_cod_sexo())          # esta ya el municipo y el sexo
            self.comboBoxGrupos.setCurrentText(str(self.estudiante.get_grupo()))
