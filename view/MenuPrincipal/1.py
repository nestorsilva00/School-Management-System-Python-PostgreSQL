# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogPrincipal(object):
    def setupUi(self, DialogPrincipal):
        DialogPrincipal.setObjectName("DialogPrincipal")
        DialogPrincipal.resize(710, 499)
        DialogPrincipal.setStyleSheet("QLabel{\n"
"background-color: rgb(51, 103, 145);\n"
"}\n"
"\n"
"QPushButtom{\n"
"border-radius:12px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame = QtWidgets.QFrame(DialogPrincipal)
        self.frame.setGeometry(QtCore.QRect(0, 0, 711, 501))
        self.frame.setStyleSheet("QLabel{\n"
"background-color: rgb(51, 103, 145);\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-right:2px solid rgb(170, 170, 170);\n"
"border-bottom:2px solid rgb(170, 170, 170);\n"
"}\n"
"\n"
"QFrame{\n"
"border:1px solid  rgb(148, 148, 148);\n"
"border-radius:12px;\n"
"}\n"
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
        self.frameDatos = QtWidgets.QFrame(self.frame)
        self.frameDatos.setGeometry(QtCore.QRect(10, 70, 341, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frameDatos.setFont(font)
        self.frameDatos.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(112, 112, 112);\n"
"}\n"
"")
        self.frameDatos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDatos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDatos.setObjectName("frameDatos")
        self.labelDatosImg = QtWidgets.QLabel(self.frameDatos)
        self.labelDatosImg.setGeometry(QtCore.QRect(0, 0, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelDatosImg.setFont(font)
        self.labelDatosImg.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-right:2px solid rgb(170, 170, 170);\n"
"border-bottom:2px solid rgb(170, 170, 170);\n"
"}")
        self.labelDatosImg.setText("")
        self.labelDatosImg.setPixmap(QtGui.QPixmap(":/iconos/icons8_Add_Property_48.png"))
        self.labelDatosImg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDatosImg.setIndent(-5)
        self.labelDatosImg.setObjectName("labelDatosImg")
        self.pushButtonEstudiantes = QtWidgets.QPushButton(self.frameDatos)
        self.pushButtonEstudiantes.setGeometry(QtCore.QRect(60, 70, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButtonEstudiantes.setFont(font)
        self.pushButtonEstudiantes.setStyleSheet("")
        self.pushButtonEstudiantes.setCheckable(False)
        self.pushButtonEstudiantes.setObjectName("pushButtonEstudiantes")
        self.labelDatos = QtWidgets.QLabel(self.frameDatos)
        self.labelDatos.setGeometry(QtCore.QRect(20, 5, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelDatos.setFont(font)
        self.labelDatos.setStyleSheet("border: 0px;\n"
"")
        self.labelDatos.setObjectName("labelDatos")
        self.pushButtonAsignaturas = QtWidgets.QPushButton(self.frameDatos)
        self.pushButtonAsignaturas.setGeometry(QtCore.QRect(60, 120, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAsignaturas.setFont(font)
        self.pushButtonAsignaturas.setObjectName("pushButtonAsignaturas")
        self.pushButtonCursos = QtWidgets.QPushButton(self.frameDatos)
        self.pushButtonCursos.setGeometry(QtCore.QRect(60, 170, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCursos.setFont(font)
        self.pushButtonCursos.setObjectName("pushButtonCursos")
        self.pushButton_5 = QtWidgets.QPushButton(self.frameDatos)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 220, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.frameReportes = QtWidgets.QFrame(self.frame)
        self.frameReportes.setGeometry(QtCore.QRect(370, 70, 331, 421))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.frameReportes.setFont(font)
        self.frameReportes.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(112, 112, 112);\n"
"}\n"
"")
        self.frameReportes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameReportes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameReportes.setLineWidth(0)
        self.frameReportes.setObjectName("frameReportes")
        self.labelReportesImg = QtWidgets.QLabel(self.frameReportes)
        self.labelReportesImg.setGeometry(QtCore.QRect(0, 0, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelReportesImg.setFont(font)
        self.labelReportesImg.setText("")
        self.labelReportesImg.setPixmap(QtGui.QPixmap(":/iconos/icons8_PDF_48.png"))
        self.labelReportesImg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelReportesImg.setObjectName("labelReportesImg")
        self.label_2 = QtWidgets.QLabel(self.frameReportes)
        self.label_2.setGeometry(QtCore.QRect(20, 5, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:0px;")
        self.label_2.setObjectName("label_2")
        self.pushButtonListAlumGrupo = QtWidgets.QPushButton(self.frameReportes)
        self.pushButtonListAlumGrupo.setGeometry(QtCore.QRect(60, 60, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonListAlumGrupo.setFont(font)
        self.pushButtonListAlumGrupo.setObjectName("pushButtonListAlumGrupo")
        self.pushButtonListAsigAnno = QtWidgets.QPushButton(self.frameReportes)
        self.pushButtonListAsigAnno.setGeometry(QtCore.QRect(60, 100, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonListAsigAnno.setFont(font)
        self.pushButtonListAsigAnno.setObjectName("pushButtonListAsigAnno")
        self.pushButtonEvaGrupo = QtWidgets.QPushButton(self.frameReportes)
        self.pushButtonEvaGrupo.setGeometry(QtCore.QRect(60, 140, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEvaGrupo.setFont(font)
        self.pushButtonEvaGrupo.setObjectName("pushButtonEvaGrupo")
        self.pushButton_3 = QtWidgets.QPushButton(self.frameReportes)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 180, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frameReportes)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 220, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frameReportes)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frameReportes)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 300, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frameReportes)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 340, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frameReportes)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 380, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.LabelEncabezado = QtWidgets.QLabel(self.frame)
        self.LabelEncabezado.setGeometry(QtCore.QRect(0, 0, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LabelEncabezado.setFont(font)
        self.LabelEncabezado.setStyleSheet("")
        self.LabelEncabezado.setObjectName("LabelEncabezado")
        self.PushButtomCambiarCon = QtWidgets.QPushButton(self.frame)
        self.PushButtomCambiarCon.setGeometry(QtCore.QRect(540, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PushButtomCambiarCon.setFont(font)
        self.PushButtomCambiarCon.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/icons8_Key_48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.PushButtomCambiarCon.setObjectName("PushButtomCambiarCon")

        self.retranslateUi(DialogPrincipal)
        QtCore.QMetaObject.connectSlotsByName(DialogPrincipal)

    def retranslateUi(self, DialogPrincipal):
        _translate = QtCore.QCoreApplication.translate
        DialogPrincipal.setWindowTitle(_translate("DialogPrincipal", "Dialog"))
        self.pushButtonEstudiantes.setText(_translate("DialogPrincipal", "Estudiantes"))
        self.labelDatos.setText(_translate("DialogPrincipal", "Datos"))
        self.pushButtonAsignaturas.setText(_translate("DialogPrincipal", "Asignaturas"))
        self.pushButtonCursos.setText(_translate("DialogPrincipal", "Cursos"))
        self.pushButton_5.setText(_translate("DialogPrincipal", "Años"))
        self.label_2.setText(_translate("DialogPrincipal", "Reportes"))
        self.pushButtonListAlumGrupo.setText(_translate("DialogPrincipal", "Listado de alumnos por grupo"))
        self.pushButtonListAsigAnno.setText(_translate("DialogPrincipal", "Listado de asignaturas por año"))
        self.pushButtonEvaGrupo.setText(_translate("DialogPrincipal", "Evaluaciones por grupo"))
        self.pushButton_3.setText(_translate("DialogPrincipal", "PushButton"))
        self.pushButton_4.setText(_translate("DialogPrincipal", "PushButton"))
        self.pushButton_6.setText(_translate("DialogPrincipal", "PushButton"))
        self.pushButton_7.setText(_translate("DialogPrincipal", "PushButton"))
        self.pushButton_8.setText(_translate("DialogPrincipal", "PushButton"))
        self.pushButton_9.setText(_translate("DialogPrincipal", "PushButton"))
        self.LabelEncabezado.setText(_translate("DialogPrincipal", "      Bienvenido"))
        self.PushButtomCambiarCon.setText(_translate("DialogPrincipal", "Cambiar contraseña"))
import iconos_rc
