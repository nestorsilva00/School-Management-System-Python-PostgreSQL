# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grupos.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from service.Grupo_Service import Grupo_Service
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


class Ui_Grupos(object):
    def setupUi(self, Grupos):
        Grupos.setObjectName("Grupos")
        Grupos.resize(452, 405)
        Grupos.setMinimumSize(QtCore.QSize(452, 405))
        Grupos.setMaximumSize(QtCore.QSize(452, 405))
        Grupos.setStyleSheet("QLabel{\n"
"border-radius:12px;\n"
"background-color: rgb(51, 103, 145);\n"
"\n"
"}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Grupos)
        self.label.setGeometry(QtCore.QRect(10, 19, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Grupos)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 281, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frameFunciones = QtWidgets.QFrame(Grupos)
        self.frameFunciones.setGeometry(QtCore.QRect(310, 70, 131, 121))
        self.frameFunciones.setStyleSheet("QFrame{\n"
"border-radius:12px;\n"
"border:1px solid rgb(112, 112, 112);\n"
"}\n"
"\n"
"QLabel{\n"
"border-radius:12px;\n"
"background-color: rgb(234, 234, 234);\n"
"\n"
"}\n"
"QPushButton{\n"
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
"\n"
"")
        self.frameFunciones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFunciones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFunciones.setObjectName("frameFunciones")
        self.pushButtonInsertar = QtWidgets.QPushButton(self.frameFunciones)
        self.pushButtonInsertar.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInsertar.setFont(font)
        self.pushButtonInsertar.setStyleSheet("")
        self.pushButtonInsertar.setObjectName("pushButtonInsertar")
        self.comboBox = QtWidgets.QComboBox(self.frameFunciones)
        self.comboBox.setGeometry(QtCore.QRect(20, 70, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.frameFunciones_2 = QtWidgets.QFrame(Grupos)
        self.frameFunciones_2.setGeometry(QtCore.QRect(310, 200, 131, 71))
        self.frameFunciones_2.setStyleSheet("QFrame{\n"
"border-radius:12px;\n"
"border:1px solid rgb(112, 112, 112);\n"
"}\n"
"\n"
"QLabel{\n"
"border-radius:12px;\n"
"background-color: rgb(234, 234, 234);\n"
"\n"
"}\n"
"QPushButton{\n"
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
"\n"
"")
        self.frameFunciones_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFunciones_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFunciones_2.setObjectName("frameFunciones_2")
        self.pushButtonEliminar = QtWidgets.QPushButton(self.frameFunciones_2)
        self.pushButtonEliminar.setGeometry(QtCore.QRect(20, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEliminar.setFont(font)
        self.pushButtonEliminar.setStyleSheet("")
        self.pushButtonEliminar.setObjectName("pushButtonEliminar")
        self.retranslateUi(Grupos)
        QtCore.QMetaObject.connectSlotsByName(Grupos)
        self.cargar_tabla()
        self.cargar_comboBox()
        self.pushButtonInsertar.clicked.connect(self.on_pushButtonInsertar_clicked)
        self.pushButtonEliminar.clicked.connect(self.on_pushButtonEliminar_clicked)


    def retranslateUi(self, Grupos):
        _translate = QtCore.QCoreApplication.translate
        Grupos.setWindowTitle(_translate("Grupos", "Grupos"))
        self.label.setText(_translate("Grupos", "Grupos"))
        self.pushButtonInsertar.setText(_translate("Grupos", "Insertar"))
        self.pushButtonEliminar.setText(_translate("Grupos", "Eliminar"))

    def cargar_tabla(self):
        grupos = Grupo_Service.get_grupos_ultimo_curso(Grupo_Service)
        x = 1
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(x)
        self.tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem("código de grupo"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("grupo"))
        for i in grupos:
            self.tableWidget.setRowCount(x)
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setItem(x - 1, 0, QTableWidgetItem(str(i.cod_grupo)))
            self.tableWidget.setItem(x - 1, 1, QTableWidgetItem(str(i.num_grupo)))
            x += 1

        self.tableWidget.setCurrentItem(None)

    def cargar_comboBox(self):
        anno = self.annos_existentes()
        i=1
        while(i<=anno):
            self.comboBox.addItem(str(i))
            i+=1

    def annos_existentes(self):
        grupos = Grupo_Service.get_grupos_ultimo_curso(Grupo_Service)
        mayor = 0
        for i in grupos:
            if i.num_grupo > mayor:
                mayor = i.num_grupo

        string = str(mayor)
        separado = int(string[0])
        return separado

    def on_pushButtonInsertar_clicked(self):
        anno = self.comboBox.currentText()
        datos_grupo = self.datos_annos_insertar(anno)
        Grupo_Service.create_grupo(Grupo_Service,datos_grupo[0]+1,datos_grupo[1])
        self.cargar_tabla()

    def datos_annos_insertar(self,anno):
        grupos = Grupo_Service.get_grupos_ultimo_curso(Grupo_Service)
        mayor_grupo = 0
        cod_mayor_grupo = 0
        datos_grupo = []
        for i in grupos:
            if str(i.num_grupo)[0] == str(anno):
                if i.num_grupo > mayor_grupo:
                    mayor_grupo = i.num_grupo
                    cod_mayor_grupo = i.cod_anno

        datos_grupo.append(mayor_grupo)
        datos_grupo.append(cod_mayor_grupo)
        return datos_grupo

    def on_pushButtonEliminar_clicked(self):
        if self.tableWidget.currentRow() == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Seleccione un grupo")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            index = self.tableWidget.currentRow()
            cod_grupo = int(self.tableWidget.item(index, 0).text())
            is_asignaciones = Grupo_Service.isAsignacionesGrupo(Grupo_Service,int(cod_grupo))
            if is_asignaciones:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("El grupo tiene estudiantes asignados,no puede ser eliminado")
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                Grupo_Service.delete_grupo(Grupo_Service,cod_grupo)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("El grupo ha sido eliminado")
                msg.setWindowTitle("Información")
                msg.exec_()

        self.cargar_tabla()



