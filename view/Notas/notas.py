# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notas.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from service.Asignatura_Service import Asignatura_Service
from service.Evaluacion_Service import Evaluacion_Service
from service.Nota_Service import Nota_Service
from service.Estudiante_Service import Estudiante_Service
from service.Anno_Service import Anno_Service
from service.Curso_Service import Curso_Service


class Ui_DialogNotas(object):
    def setupUi(self, DialogNotas,est):
        self.estudiante = est
        DialogNotas.setObjectName("DialogNotas")
        DialogNotas.resize(652, 400)
        DialogNotas.setStyleSheet("QDialog{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
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
"QComboBox{\n"
"border-radius:2px;\n"
"border:1px solid grey;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(DialogNotas)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(51, 103, 145);\n"
"border-radius:15px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidgetNotas = QtWidgets.QTableWidget(DialogNotas)
        self.tableWidgetNotas.setGeometry(QtCore.QRect(10, 70, 271, 281))
        self.tableWidgetNotas.setObjectName("tableWidgetNotas")
        self.tableWidgetNotas.setColumnCount(2)
        self.tableWidgetNotas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNotas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNotas.setHorizontalHeaderItem(1, item)
        self.pushButtonSalir = QtWidgets.QPushButton(DialogNotas)
        self.pushButtonSalir.setGeometry(QtCore.QRect(10, 360, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSalir.setFont(font)
        self.pushButtonSalir.setStyleSheet("background-color: rgb(255, 21, 21);")
        self.pushButtonSalir.setObjectName("pushButtonSalir")
        self.label_2 = QtWidgets.QLabel(DialogNotas)
        self.label_2.setGeometry(QtCore.QRect(370, 70, 271, 281))
        self.label_2.setStyleSheet("QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid grey;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButtonInsertar = QtWidgets.QPushButton(DialogNotas)
        self.pushButtonInsertar.setGeometry(QtCore.QRect(290, 170, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInsertar.setFont(font)
        self.pushButtonInsertar.setObjectName("pushButtonInsertar")
        self.pushButtonEliminar = QtWidgets.QPushButton(DialogNotas)
        self.pushButtonEliminar.setGeometry(QtCore.QRect(290, 210, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEliminar.setFont(font)
        self.pushButtonEliminar.setObjectName("pushButtonEliminar")
        self.label_3 = QtWidgets.QLabel(DialogNotas)
        self.label_3.setGeometry(QtCore.QRect(370, 70, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(51, 103, 145);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.labelAsignaturas = QtWidgets.QLabel(DialogNotas)
        self.labelAsignaturas.setGeometry(QtCore.QRect(390, 120, 91, 21))
        self.labelAsignaturas.setObjectName("labelAsignaturas")
        self.labelEvaluacion = QtWidgets.QLabel(DialogNotas)
        self.labelEvaluacion.setGeometry(QtCore.QRect(390, 170, 91, 21))
        self.labelEvaluacion.setObjectName("labelEvaluacion")
        self.comboBox = QtWidgets.QComboBox(DialogNotas)
        self.comboBox.setGeometry(QtCore.QRect(510, 120, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(DialogNotas)
        self.comboBox_2.setGeometry(QtCore.QRect(510, 170, 111, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.retranslateUi(DialogNotas)
        QtCore.QMetaObject.connectSlotsByName(DialogNotas)
        self.cargar_comboBox_Asignaturas(est.get_cod_estudiante())
        self.cargar_comboBox_Evaluaciones()
        self.cargar_tabla_notas()
        self.pushButtonInsertar.clicked.connect(self.on_pushButtonInsertar_clicked)
        self.pushButtonEliminar.clicked.connect(self.on_pushButtonEliminar_clicked)

    def retranslateUi(self, DialogNotas):
        _translate = QtCore.QCoreApplication.translate
        DialogNotas.setWindowTitle(_translate("DialogNotas", "Dialog"))
        self.label.setText(_translate("DialogNotas", "Notas"))
        item = self.tableWidgetNotas.horizontalHeaderItem(0)
        item.setText(_translate("DialogNotas", "Asignaturas"))
        item = self.tableWidgetNotas.horizontalHeaderItem(1)
        item.setText(_translate("DialogNotas", "Notas"))
        self.pushButtonSalir.setText(_translate("DialogNotas", "Salir"))
        self.pushButtonInsertar.setText(_translate("DialogNotas", "Insertar"))
        self.pushButtonEliminar.setText(_translate("DialogNotas", "Eliminar"))
        self.label_3.setText(_translate("DialogNotas", "Selecionar datos"))
        self.labelAsignaturas.setText(_translate("DialogNotas", "Asignaturas:"))
        self.labelEvaluacion.setText(_translate("DialogNotas", "Evaluación:"))

    def cargar_comboBox_Asignaturas(self, est):
            self.comboBox.clear()
            asignaturas = Asignatura_Service.asignaturas_por_estudiante(Asignatura_Service, est)
            asignaturas_con_nota = Nota_Service.asignaturas_con_notas_por_estudiante(Asignatura_Service, est)
            asignaturas_nombres  = []
            for i in asignaturas:
                if i not in asignaturas_con_nota:
                    asignaturas_nombres.append(Asignatura_Service.get_asignatura_nombre(Asignatura_Service, i[0]))

            self.comboBox.addItems(asignaturas_nombres)
    def cargar_comboBox_Evaluaciones(self):
            evaluaciones = Evaluacion_Service.read_evaluacion(Evaluacion_Service)
            for i in evaluaciones:
                    self.comboBox_2.addItem(i.get_evaluacion())

    def on_pushButtonInsertar_clicked(self):
        if self.comboBox.currentText()== "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("No hay asignatura seleccionada")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            asignatura_seleccionada = self.comboBox.currentText()
            evaluacion_seleccionada = self.comboBox_2.currentText()
            cod_estudiante = self.estudiante.get_cod_estudiante()
            cod_asignatura = Asignatura_Service.get_cod_asignatura(Asignatura_Service, asignatura_seleccionada, cod_estudiante)
            cod_anno = Asignatura_Service.get_cod_anno(Asignatura_Service, cod_asignatura)
            cod_evaluacion = Evaluacion_Service.get_cod_evaluacion(Evaluacion_Service, evaluacion_seleccionada)
            Nota_Service.create_nota(Nota_Service, cod_asignatura,cod_estudiante , cod_anno, cod_evaluacion)
            self.cargar_comboBox_Asignaturas(self.estudiante.get_cod_estudiante())
            self.cargar_tabla_notas()

    def cargar_tabla_notas(self):
        self.tableWidgetNotas.clear()
        lista= Nota_Service.read_nota(Nota_Service)


        x = 1
        for i in lista:
            if i.get_cod_estudiante() == self.estudiante.get_cod_estudiante():
                self.tableWidgetNotas.setRowCount(x)
                self.tableWidgetNotas.setColumnCount(7)
                self.tableWidgetNotas.setItem(x - 1, 0, QTableWidgetItem(str(i.get_cod_asignatura())))
                self.tableWidgetNotas.setItem(x - 1, 1, QTableWidgetItem(str(Asignatura_Service.get_asignatura_nombre(Asignatura_Service, i.get_cod_asignatura()))))
                self.tableWidgetNotas.setItem(x - 1, 2, QTableWidgetItem(str(i.get_cod_estudiante())))
                self.tableWidgetNotas.setItem(x - 1, 3, QTableWidgetItem(str(Estudiante_Service.get_nombre_estudiante(Estudiante_Service, i.get_cod_estudiante()))))
                self.tableWidgetNotas.setItem(x - 1, 4, QTableWidgetItem(str(i.get_cod_anno())))
                self.tableWidgetNotas.setItem(x - 1, 5, QTableWidgetItem(str(Anno_Service.get_anno(Anno_Service, i.get_cod_anno()))))
                self.tableWidgetNotas.setItem(x - 1, 6, QTableWidgetItem(str(i.get_cod_evaluacion())))
                x += 1

        self.tableWidgetNotas.setCurrentItem(None)

    def on_pushButtonEliminar_clicked(self):
        if self.tableWidgetNotas.currentRow() == -1:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Seleccione una nota")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            index = self.tableWidgetNotas.currentRow()
            cod_asignatura = self.tableWidgetNotas.item(index, 0).text()
            cod_estudiante = self.tableWidgetNotas.item(index, 2).text()
            cod_anno = self.tableWidgetNotas.item(index, 4).text()
            self.tableWidgetNotas.setCurrentItem(None)
            Nota_Service.delete_nota(Nota_Service, int(cod_asignatura), int(cod_estudiante), int(cod_anno))
            self.cargar_tabla_notas()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Nota eliminado correctamente")
            msg.setWindowTitle("Información")
            msg.exec_()
            self.cargar_comboBox_Asignaturas(self.estudiante.get_cod_estudiante())