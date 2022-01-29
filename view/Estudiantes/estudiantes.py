# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estudiantes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox,QDialog
from reports import Certificacion_de_notas


from model.Anno import Anno
from model.Grupo import *
from model.Estudiante import *
from service.Curso_Service import *
from service.Estudiante_Service import *
from service.Anno_Service import *
from service.Sexo_Service import *
from service.Municipio_Service import *
from view.Baja.baja import Ui_dlgBaja
from view.InsertarEstudiante.insertar import Ui_DialogInsertarEstudiante
from view.ModificarEstudiante.modificarEstudiante import Ui_DialogModificarEstudiante
from view.Notas.notas import Ui_DialogNotas


class Ui_DialogEstudiantes(object):
    def setupUi(self, Dialog,escribir):
        self.escribir = escribir
        self.d = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 621)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(740, 621))
        Dialog.setMaximumSize(QtCore.QSize(740, 621))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 751, 621))
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(1151651, 16777215))
        self.frame.setStyleSheet("QPushButton{\n"
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
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableView(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(190, 110, 541, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.model = QtGui.QStandardItemModel(self.tableWidget)
        self.model.setHorizontalHeaderLabels(["Código", "Nombre", "Apellidos", "Municipio", "Sexo"])

        self.frameFunciones = QtWidgets.QFrame(self.frame)
        self.frameFunciones.setGeometry(QtCore.QRect(10, 10, 721, 91))
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
                                          "\n"
                                          "\n"
                                          "")
        self.frameFunciones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFunciones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFunciones.setObjectName("frameFunciones")
        self.pushButtonInsertar = QtWidgets.QPushButton(self.frameFunciones)
        self.pushButtonInsertar.setGeometry(QtCore.QRect(10, 50, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInsertar.setFont(font)
        self.pushButtonInsertar.setStyleSheet("")
        self.pushButtonInsertar.setObjectName("pushButtonInsertar")
        self.pushButtonModificar = QtWidgets.QPushButton(self.frameFunciones)
        self.pushButtonModificar.setGeometry(QtCore.QRect(120, 50, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificar.setFont(font)
        self.pushButtonModificar.setStyleSheet("")
        self.pushButtonModificar.setObjectName("pushButtonModificar")
        self.pushButtonEliminar = QtWidgets.QPushButton(self.frameFunciones)
        self.pushButtonEliminar.setGeometry(QtCore.QRect(230, 50, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEliminar.setFont(font)
        self.pushButtonEliminar.setStyleSheet("")
        self.pushButtonEliminar.setObjectName("pushButtonEliminar")

        self.pushButtonReporteNotas = QtWidgets.QPushButton(self.frameFunciones)
        self.pushButtonReporteNotas.setGeometry(QtCore.QRect(450, 50, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonReporteNotas.setFont(font)
        self.pushButtonReporteNotas.setObjectName("pushButtonReporteNotas")

        self.pushButtonBaja = QtWidgets.QPushButton(self.frameFunciones)
        self.pushButtonBaja.setGeometry(QtCore.QRect(340, 50, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBaja.setFont(font)
        self.pushButtonBaja.setObjectName("pushButtonBaja")

        self.labelFunciones = QtWidgets.QLabel(self.frameFunciones)
        self.labelFunciones.setGeometry(QtCore.QRect(0, 0, 721, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelFunciones.setFont(font)
        self.labelFunciones.setStyleSheet("background-color: rgb(51, 103, 145);")
        self.labelFunciones.setTextFormat(QtCore.Qt.PlainText)
        self.labelFunciones.setScaledContents(False)
        self.labelFunciones.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFunciones.setObjectName("labelFunciones")
        self.pushButtonNotas = QtWidgets.QPushButton(self.frameFunciones)
        self.pushButtonNotas.setGeometry(QtCore.QRect(610, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonNotas.setFont(font)
        self.pushButtonNotas.setObjectName("pushButtonNotas")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 580, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 21, 21);")
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frameFiltro = QtWidgets.QFrame(self.frame)
        self.frameFiltro.setGeometry(QtCore.QRect(10, 110, 171, 461))
        self.frameFiltro.setStyleSheet("QFrame#frameFiltro{\n"
                                       "border-radius:12px;\n"
                                       "border:1px solid rgb(112, 112, 112);\n"
                                       "}")
        self.frameFiltro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFiltro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFiltro.setObjectName("frameFiltro")
        self.frameEstado = QtWidgets.QFrame(self.frameFiltro)
        self.frameEstado.setGeometry(QtCore.QRect(10, 50, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.frameEstado.setFont(font)
        self.frameEstado.setStyleSheet("QLabel{\n"
                                       "boder-radius:3px\n"
                                       "}")
        self.frameEstado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameEstado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEstado.setObjectName("frameEstado")
        self.labelEstado = QtWidgets.QLabel(self.frameEstado)
        self.labelEstado.setGeometry(QtCore.QRect(0, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelEstado.setFont(font)
        self.labelEstado.setStyleSheet("background-color: rgb(51, 103, 145);\n"
                                       "")
        self.labelEstado.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEstado.setObjectName("labelEstado")
        self.comboBoxEstado = QtWidgets.QComboBox(self.frameEstado)
        self.comboBoxEstado.setGeometry(QtCore.QRect(10, 40, 131, 22))
        self.comboBoxEstado.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBoxEstado.setObjectName("comboBoxEstado")
        self.labelFiltro = QtWidgets.QLabel(self.frameFiltro)
        self.labelFiltro.setGeometry(QtCore.QRect(0, 0, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelFiltro.setFont(font)
        self.labelFiltro.setStyleSheet("background-color: rgb(51, 103, 145);\n"
                                       "border-radius:15px")
        self.labelFiltro.setTextFormat(QtCore.Qt.PlainText)
        self.labelFiltro.setScaledContents(False)
        self.labelFiltro.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFiltro.setObjectName("labelFiltro")
        self.frameCursoAnnoGrupo = QtWidgets.QFrame(self.frameFiltro)
        self.frameCursoAnnoGrupo.setGeometry(QtCore.QRect(10, 200, 151, 211))
        self.frameCursoAnnoGrupo.setStyleSheet("QLabel{\n"
                                               "background-color: rgb(51, 103, 145);\n"
                                               "}")
        self.frameCursoAnnoGrupo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCursoAnnoGrupo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCursoAnnoGrupo.setObjectName("frameCursoAnnoGrupo")
        self.labelGrupos = QtWidgets.QLabel(self.frameCursoAnnoGrupo)
        self.labelGrupos.setGeometry(QtCore.QRect(0, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelGrupos.setFont(font)
        self.labelGrupos.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGrupos.setObjectName("labelGrupos")
        self.labelCursos = QtWidgets.QLabel(self.frameCursoAnnoGrupo)
        self.labelCursos.setGeometry(QtCore.QRect(-6, -1, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelCursos.setFont(font)
        self.labelCursos.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCursos.setObjectName("labelCursos")
        self.labelAnnos = QtWidgets.QLabel(self.frameCursoAnnoGrupo)
        self.labelAnnos.setGeometry(QtCore.QRect(-6, 69, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelAnnos.setFont(font)
        self.labelAnnos.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnnos.setObjectName("labelAnnos")
        self.comboBoxCursos = QtWidgets.QComboBox(self.frameCursoAnnoGrupo)
        self.comboBoxCursos.setGeometry(QtCore.QRect(10, 40, 131, 22))
        self.comboBoxCursos.setObjectName("comboBoxCursos")
        self.comboBoxAnnos = QtWidgets.QComboBox(self.frameCursoAnnoGrupo)
        self.comboBoxAnnos.setGeometry(QtCore.QRect(10, 110, 131, 22))
        self.comboBoxAnnos.setObjectName("comboBoxAnnos")
        self.comboBoxGrupos = QtWidgets.QComboBox(self.frameCursoAnnoGrupo)
        self.comboBoxGrupos.setGeometry(QtCore.QRect(10, 180, 131, 21))
        self.comboBoxGrupos.setObjectName("comboBoxGrupos")
        self.pushButtonFiltar = QtWidgets.QPushButton(self.frameFiltro)
        self.pushButtonFiltar.setGeometry(QtCore.QRect(40, 420, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonFiltar.setFont(font)
        self.pushButtonFiltar.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButtonFiltar.setObjectName("pushButtonFiltar")
        self.frameEstado_2 = QtWidgets.QFrame(self.frameFiltro)
        self.frameEstado_2.setGeometry(QtCore.QRect(10, 130, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.frameEstado_2.setFont(font)
        self.frameEstado_2.setStyleSheet("QLabel{\n"
                                         "boder-radius:3px\n"
                                         "}")
        self.frameEstado_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameEstado_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEstado_2.setObjectName("frameEstado_2")
        self.labelSexo = QtWidgets.QLabel(self.frameEstado_2)
        self.labelSexo.setGeometry(QtCore.QRect(0, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelSexo.setFont(font)
        self.labelSexo.setStyleSheet("background-color: rgb(51, 103, 145);\n"
                                     "")
        self.labelSexo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSexo.setObjectName("labelSexo")
        self.comboBoxSexo = QtWidgets.QComboBox(self.frameEstado_2)
        self.comboBoxSexo.setGeometry(QtCore.QRect(8, 40, 131, 22))
        self.comboBoxSexo.setObjectName("comboBoxSexo")
        self.municipios = dict()
        self.sexos = dict()


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # -----------------
        self.pushButtonInsertar.clicked.connect(self.on_pushButtonInsertar_clicked)
        self.pushButtonModificar.clicked.connect(self.on_pushButtonModificar_clicked)
        self.pushButtonEliminar.clicked.connect(self.on_pushButtonEliminar_clicked)
        self.pushButton.clicked.connect(self.d.close)
        self.pushButtonFiltar.clicked.connect(self.cargar_tabla)
        self.pushButtonNotas.clicked.connect(self.on_pushButtonNotas_clicked)
        self.comboBoxCursos.activated.connect(self.cargar_comboBox_Annos)
        self.comboBoxAnnos.activated.connect(self.cargar_comboBox_grupos)
        self.pushButtonReporteNotas.clicked.connect(self.on_pushButtonReportNotas_clicked)
        self.pushButtonBaja.clicked.connect(self.on_pushButtonBaja_clicked)
        self.cargar_municipios()
        self.cargar_sexos()
        self.cargar_comboBox_estados()
        self.cargar_comboBox_sexo()
        self.cargar_comboBox_cursos()
        self.cargar_tabla()
        self.canEscribir()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Estudiantes"))
        self.pushButtonInsertar.setText(_translate("Dialog", "Insertar"))
        self.pushButtonModificar.setText(_translate("Dialog", "Modificar"))
        self.pushButtonEliminar.setText(_translate("Dialog", "Eliminar"))
        self.labelFunciones.setText(_translate("Dialog", "Funciones"))
        self.pushButtonNotas.setText(_translate("Dialog", "Notas"))
        self.pushButton.setText(_translate("Dialog", "Salir"))
        self.labelAnnos.setText(_translate("Dialog", "Años"))
        self.labelFiltro.setText(_translate("Dialog", "Filtro"))
        self.labelEstado.setText(_translate("Dialog", "Estado"))
        self.labelSexo.setText(_translate("Dialog", "Sexo"))
        self.labelCursos.setText(_translate("Dialog", "Cursos"))
        self.labelGrupos.setText(_translate("Dialog", "Grupos"))
        self.pushButtonFiltar.setText(_translate("Dialog", "Filtrar"))
        self.pushButtonReporteNotas.setText(_translate("Dialog", "Certificación de Notas"))
        self.pushButtonBaja.setText(_translate("Dialog", "Baja"))

    def on_pushButtonInsertar_clicked(self):
        ins = QDialog()
        ui = Ui_DialogInsertarEstudiante()
        ui.setupUi(ins, )
        ins.exec_()
        self.cargar_tabla()

    def on_pushButtonModificar_clicked(self):
        if self.tableWidget.currentIndex().row() == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Seleccione un estudiante")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            i = self.tableWidget.selectedIndexes()
            row = i[0].row()
            cod_est = int(self.model.data(self.model.index(row, 0)))
            nombre = self.model.data(self.model.index(row, 1))
            apell = self.model.data(self.model.index(row, 2))
            municipio = self.model.data(self.model.index(row, 3))
            sexo = self.model.data(self.model.index(row, 4))
            if Estudiante_Service.isBaja(cod_est)==False:
                est = Estudiante(cod_est, nombre, apell, sexo, municipio)

                ins = QDialog()
                ui = Ui_DialogModificarEstudiante()
                ui.setupUi(ins, est)
                ins.exec_()
                self.cargar_tabla()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Este estudiante ya ha sido dado de Baja")
                msg.setWindowTitle("Error")
                msg.exec_()
                self.cargar_tabla()


    def on_pushButtonEliminar_clicked(self):
        if self.tableWidget.currentIndex().row() == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Seleccione un estudiante")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            i = self.tableWidget.selectedIndexes()
            row = i[0].row()
            cod_est = int(self.model.data(self.model.index(row, 0)))
            Estudiante_Service.delete_estudiante(Estudiante_Service, int(cod_est))
            self.cargar_tabla()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Estudiante eliminado correctamente")
            msg.setWindowTitle("Información")
            msg.exec_()
        self.cargar_tabla()



    def on_pushButtonNotas_clicked(self):
        if self.tableWidget.currentIndex().row() == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Seleccione un estudiante")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            i = self.tableWidget.selectedIndexes()
            row = i[0].row()
            cod_est = int(self.model.data(self.model.index(row, 0)))
            nombre = self.model.data(self.model.index(row, 1))
            apell =self.model.data(self.model.index(row, 2))
            municipio =self.model.data(self.model.index(row, 3))
            sexo = self.model.data(self.model.index(row, 4))
            est = Estudiante(cod_est, nombre, apell, sexo, municipio)
            dlgNotas = QtWidgets.QDialog()
            ui = Ui_DialogNotas()
            ui.setupUi(dlgNotas,est)
            dlgNotas.exec_()
        self.cargar_tabla()


    def cargar_tabla(self):
        curso = self.comboBoxCursos.currentText()
        anno = self.comboBoxAnnos.currentText()
        grupo = self.comboBoxGrupos.currentText()
        estado = self.comboBoxEstado.currentText()
        sexo = self.comboBoxSexo.currentText()
        self.model.clear()


        if(sexo != "Todos"):
            lista = Estudiante_Service.get_estudinates_filtrados_un_sexo(Estudiante_Service,curso,anno,grupo,sexo)
            lista = self.filtrar_estudiantes_por_estado(lista,estado)
            for i in lista:
                items = []
                items.append(QtGui.QStandardItem(str(i[0].get_cod_estudiante())))
                items.append(QtGui.QStandardItem(i[0].get_nom_estudiante()))
                items.append(QtGui.QStandardItem(i[0].get_apellidos()))
                items.append(QtGui.QStandardItem(str(self.municipios[i[0].get_cod_municipio()])))
                items.append(QtGui.QStandardItem(str(self.sexos[i[0].get_cod_sexo()])))
                self.model.appendRow(items)
            self.tableWidget.setModel(self.model)
            self.tableWidget.setCurrentIndex(self.tableWidget.model().index(-1, -1))

        else:
            lista = Estudiante_Service.get_estudinates_filtrados_ambos_sexos(Estudiante_Service,curso, anno, grupo)
            lista = self.filtrar_estudiantes_por_estado(lista, estado)
            for i in lista:
                items = []
                items.append(QtGui.QStandardItem(str(i[0].get_cod_estudiante())))
                items.append(QtGui.QStandardItem(i[0].get_nom_estudiante()))
                items.append(QtGui.QStandardItem(i[0].get_apellidos()))
                items.append(QtGui.QStandardItem(str(self.municipios[i[0].get_cod_municipio()])))
                items.append(QtGui.QStandardItem(str(self.sexos[i[0].get_cod_sexo()])))
                self.model.appendRow(items)
            self.tableWidget.setModel(self.model)
            self.tableWidget.setCurrentIndex(self.tableWidget.model().index(-1, -1))


    def filtrar_estudiantes_por_estado(self,lista,estado):
        if(estado == "Todos"):
            return lista
        elif(estado == "Activo"):
            lista1 = []
            for e in lista:
                if(e[1] == None):
                    lista1.append(e)
            return lista1
        else:
            lista1 = []
            for e in lista:
                if(e[1] != None):
                    lista1.append(e)
            return lista1

    def cargar_comboBox_estados(self):
        estados = ['Todos', 'Activo', 'Baja']
        self.comboBoxEstado.addItems(estados)

    def cargar_comboBox_sexo(self):
        sexos = ['Todos', 'Masculino', 'Femenino']
        self.comboBoxSexo.addItems(sexos)

    def cargar_comboBox_cursos(self):
        cursos = Curso_Service.Curso_Service.read_curso(Curso_Service)
        self.comboBoxCursos.addItem('Todos')
        for curso in cursos:
            self.comboBoxCursos.addItem(curso.get_curso())
        self.cargar_comboBox_Annos()

    def cargar_comboBox_Annos(self):
        self.comboBoxAnnos.clear()
        curso_selecionado = self.comboBoxCursos.currentText()
        if curso_selecionado != "Todos":
            self.comboBoxAnnos.addItem("Todos")
            annos = Anno_Service.get_annos_x_curso(Anno_Service, curso_selecionado)
            for anno in annos:
                self.comboBoxAnnos.addItem(str(anno.get_anno()))
        self.cargar_comboBox_grupos()

    def cargar_comboBox_grupos(self):
        self.comboBoxGrupos.clear()
        anno_selecionado = self.comboBoxAnnos.currentText()
        curso_selecionado = self.comboBoxCursos.currentText()
        if anno_selecionado != "Todos" and curso_selecionado != "Todos":
            self.comboBoxGrupos.addItem("Todos")
            grupos = Grupo.Grupo.grupos_por_anno(Grupo.Grupo, curso_selecionado,int(anno_selecionado))
            for grupo in grupos:
                self.comboBoxGrupos.addItem(str(grupo[0]))

    def on_pushButtonReportNotas_clicked(self):
        if self.tableWidget.currentIndex().row() == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Seleccione un estudiante")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            i = self.tableWidget.selectedIndexes()
            row = i[0].row()
            cod_est = int(self.model.data(self.model.index(row, 0)))
            nombre = self.model.data(self.model.index(row, 1))
            apell = self.model.data(self.model.index(row, 2))
            Certificacion_de_notas.report_certificacion_de_notas(cod_est,nombre, apell)
        self.cargar_tabla()

    def on_pushButtonBaja_clicked(self):
        if self.tableWidget.currentIndex().row() == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Seleccione un estudiante")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            i = self.tableWidget.selectedIndexes()
            row = i[0].row()
            cod_est = int(self.model.data(self.model.index(row, 0)))
            isBaja = Estudiante_Service.isBaja(cod_est)
            dlgBaja = QtWidgets.QDialog()
            ui = Ui_dlgBaja()
            ui.setupUi(dlgBaja, cod_est,isBaja)
            dlgBaja.exec()
        self.cargar_tabla()

    def cargar_municipios(self):
        lista_municipios_nombre = []
        lista_municipios_cod = []
        for i in Municipio_Service.read_municipio(Municipio_Service):
            lista_municipios_nombre.append(i.get_municipio())
            lista_municipios_cod.append(i.get_cod_municipio())

        for i in range(len(lista_municipios_nombre)):
            self.municipios.setdefault(lista_municipios_cod[i], lista_municipios_nombre[i])

    def cargar_sexos(self):
            lista_sexos_nombre = []
            lista_sexos_cod = []
            for i in Sexo_Service.read_sexo(Sexo_Service):
                lista_sexos_nombre.append(i.get_sexo())
                lista_sexos_cod.append(i.get_cod_sexo())

            for i in range(len(lista_sexos_nombre)):
                self.sexos.setdefault(lista_sexos_cod[i], lista_sexos_nombre[i])


    def canEscribir(self):
        self.pushButtonBaja.setEnabled(self.escribir)
        self.pushButtonNotas.setEnabled(self.escribir)
        self.pushButtonEliminar.setEnabled(self.escribir)
        self.pushButtonInsertar.setEnabled(self.escribir)
        self.pushButtonModificar.setEnabled(self.escribir)