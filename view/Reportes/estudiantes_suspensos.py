# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estudiantes_suspensos.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from service.Curso_Service import Curso_Service
from service.Grupo_Service import Grupo_Service
from service.Anno_Service import Anno_Service
from model.Anno import Anno
from model.Grupo import Grupo
from reports import Estudiantes_suspensos_por_grupo



class Ui_DialogEstudiantes_suspensos(object):
    def setupUi(self, Dialog):
        self.d = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(237, 316)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.comboBox_cursos = QtWidgets.QComboBox(Dialog)
        self.comboBox_cursos.setGeometry(QtCore.QRect(50, 70, 131, 22))
        self.comboBox_cursos.setObjectName("comboBox_cursos")
        self.comboBox_annos = QtWidgets.QComboBox(Dialog)
        self.comboBox_annos.setGeometry(QtCore.QRect(50, 150, 131, 22))
        self.comboBox_annos.setObjectName("comboBox_annos")
        self.labelCursos = QtWidgets.QLabel(Dialog)
        self.labelCursos.setGeometry(QtCore.QRect(100, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelCursos.setFont(font)
        self.labelCursos.setObjectName("labelCursos")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 120, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 47, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_grupos = QtWidgets.QComboBox(Dialog)
        self.comboBox_grupos.setGeometry(QtCore.QRect(50, 220, 131, 22))
        self.comboBox_grupos.setObjectName("comboBox_grupos")
        self.Salir = QtWidgets.QPushButton(Dialog)
        self.Salir.setGeometry(QtCore.QRect(20, 270, 75, 23))
        self.Salir.setObjectName("Salir")
        self.pushButton_MostrarReporte = QtWidgets.QPushButton(Dialog)
        self.pushButton_MostrarReporte.setGeometry(QtCore.QRect(140, 270, 75, 23))
        self.pushButton_MostrarReporte.setObjectName("pushButton_MostrarReporte")

        self.cargar_comboBox_cursos()
        self.cargar_comboBox_Annos()
        self.comboBox_cursos.activated.connect(self.cargar_comboBox_Annos)
        self.comboBox_annos.activated.connect(self.cargar_comboBox_grupos)
        self.pushButton_MostrarReporte.clicked.connect(self.on_pushButtonMostrarReporte)
        self.cargar_comboBox_grupos()
        self.Salir.clicked.connect(self.d.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Estudiantes suspensos"))
        self.labelCursos.setText(_translate("Dialog", "Curso"))
        self.label.setText(_translate("Dialog", "A??o"))
        self.label_2.setText(_translate("Dialog", "Grupo"))
        self.Salir.setText(_translate("Dialog", "Salir"))
        self.pushButton_MostrarReporte.setText(_translate("Dialog", "Mostrar"))


    def cargar_comboBox_cursos(self):
        cursos = Curso_Service.read_curso(Curso_Service)
        for curso in cursos:
            self.comboBox_cursos.addItem(curso.get_curso())
        self.cargar_comboBox_Annos()

    def cargar_comboBox_Annos(self):
        self.comboBox_annos.clear()
        curso_selecionado = self.comboBox_cursos.currentText()
        annos = Anno_Service.get_annos_x_curso(Anno_Service, curso_selecionado)
        for anno in annos:
            self.comboBox_annos.addItem(str(anno.get_anno()))
        self.cargar_comboBox_grupos()

    def cargar_comboBox_grupos(self):
        self.comboBox_grupos.clear()
        anno_selecionado = self.comboBox_annos.currentText()
        curso_selecionado = self.comboBox_cursos.currentText()
        grupos = Grupo_Service.get_grupos_por_anno_y_curso(Grupo_Service, curso_selecionado,int(anno_selecionado))
        for grupo in grupos:
            self.comboBox_grupos.addItem(str(grupo[0]))

    def on_pushButtonMostrarReporte(self):

        Estudiantes_suspensos_por_grupo.estudiantes_suspensos_por_grupo(self.comboBox_cursos.currentText(),
                                    int(self.comboBox_annos.currentText()), int(self.comboBox_grupos.currentText()))
