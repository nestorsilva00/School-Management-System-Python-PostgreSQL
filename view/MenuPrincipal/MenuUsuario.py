

from PyQt5 import QtCore, QtGui, QtWidgets
from reports import Alumnos_por_grupo, Asignaturas_por_anno, Evaluaciones_grupo_asignatura
from view.CambiarContraseña.cambiar_contraseña import Ui_CambiarContrasenna
from view.Estudiantes.estudiantes import Ui_DialogEstudiantes

from view.Reportes.escalafon import Ui_DialogEscalafon
from view.Reportes.estudiantes_bajas import Ui_DialogEstudiantes_bajas
from view.Reportes.estudiantes_suspensos import Ui_DialogEstudiantes_suspensos
from view.Reportes.promedios_por_grupo import Ui_Dialog
from view.Reportes.repitentes_por_anno import Ui_Dialog_Repitentes


class Ui_DialogMenuUsuario(object):
    def setupUi(self, DialogMenuUsuario):
        DialogMenuUsuario.setObjectName("DialogMenuUsuario")
        DialogMenuUsuario.resize(541, 492)
        DialogMenuUsuario.setStyleSheet("QLabel{\n"
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
        self.LabelEncabezado = QtWidgets.QLabel(DialogMenuUsuario)
        self.LabelEncabezado.setGeometry(QtCore.QRect(0, 0, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LabelEncabezado.setFont(font)
        self.LabelEncabezado.setStyleSheet("")
        self.LabelEncabezado.setObjectName("LabelEncabezado")
        self.PushButtomCambiarCon = QtWidgets.QPushButton(DialogMenuUsuario)
        self.PushButtomCambiarCon.setGeometry(QtCore.QRect(370, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PushButtomCambiarCon.setFont(font)
        self.PushButtomCambiarCon.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/icons8_Key_48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.PushButtomCambiarCon.setIcon(icon)
        self.PushButtomCambiarCon.setObjectName("PushButtomCambiarCon")
        self.frameReportes = QtWidgets.QFrame(DialogMenuUsuario)
        self.frameReportes.setGeometry(QtCore.QRect(110, 60, 331, 421))
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
        self.labelReportesImg_2 = QtWidgets.QLabel(self.frameReportes)
        self.labelReportesImg_2.setGeometry(QtCore.QRect(0, 0, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelReportesImg_2.setFont(font)
        self.labelReportesImg_2.setText("")
        self.labelReportesImg_2.setPixmap(QtGui.QPixmap(":/iconos/icons8_PDF_48.png"))
        self.labelReportesImg_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelReportesImg_2.setObjectName("labelReportesImg_2")
        self.label_3 = QtWidgets.QLabel(self.frameReportes)
        self.label_3.setGeometry(QtCore.QRect(20, 5, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:0px;")
        self.label_3.setObjectName("label_3")
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
        self.labelReportesImg_2.raise_()
        self.pushButtonListAlumGrupo.raise_()
        self.pushButtonListAsigAnno.raise_()
        self.pushButtonEvaGrupo.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.label_3.raise_()

        self.retranslateUi(DialogMenuUsuario)
        QtCore.QMetaObject.connectSlotsByName(DialogMenuUsuario)

        self.pushButtonListAlumGrupo.clicked.connect(self.on_pushButtonListAlumGrupo)
        self.pushButtonListAsigAnno.clicked.connect(self.on_pushButtonListAsigAnno)
        self.pushButtonEvaGrupo.clicked.connect(self.on_pushButtonEvaGrupo)
        self.pushButton_3.clicked.connect(self.on_pushButton_3)
        self.pushButton_4.clicked.connect(self.on_pushButton_4)
        self.pushButton_6.clicked.connect(self.on_pushButtonEstudiantes)
        self.pushButton_7.clicked.connect(self.on_pushButton_7)
        self.pushButton_8.clicked.connect(self.on_pushButton_8)
        self.pushButton_9.clicked.connect(self.on_pushButton_9)
        self.PushButtomCambiarCon.clicked.connect(self.on_PushButtomCambiarCon)


    def retranslateUi(self, DialogMenuUsuario):
        _translate = QtCore.QCoreApplication.translate
        DialogMenuUsuario.setWindowTitle(_translate("DialogMenuUsuario", "Dialog"))
        self.LabelEncabezado.setText(_translate("DialogMenuUsuario", "      Bienvenido"))
        self.PushButtomCambiarCon.setText(_translate("DialogMenuUsuario", "Cambiar contraseña"))
        self.label_3.setText(_translate("DialogMenuUsuario", "Reportes"))
        self.pushButtonListAlumGrupo.setText(_translate("DialogMenuUsuario", "Listado de alumnos por grupo"))
        self.pushButtonListAsigAnno.setText(_translate("DialogMenuUsuario", "Listado de asignaturas por año"))
        self.pushButtonEvaGrupo.setText(_translate("DialogMenuUsuario", "Evaluaciones por grupo"))
        self.pushButton_3.setText(_translate("DialogMenuUsuario", "Promedios de estudiantes por grupo"))
        self.pushButton_4.setText(_translate("DialogMenuUsuario", "Escalafón"))
        self.pushButton_6.setText(_translate("DialogMenuUsuario", "Certificación de notas"))
        self.pushButton_7.setText(_translate("DialogMenuUsuario", "Estudiantes suspensos"))
        self.pushButton_8.setText(_translate("DialogMenuUsuario", "Estudiantes bajas"))
        self.pushButton_9.setText(_translate("DialogMenuUsuario", "Repitentes de año"))

    def on_pushButtonListAlumGrupo(self):
            Alumnos_por_grupo.report_alumnos_por_grupo()

    def on_pushButtonListAsigAnno(self):
            Asignaturas_por_anno.report_asignaturas_anno()

    def on_pushButtonEvaGrupo(self):
            Evaluaciones_grupo_asignatura.report_evaluaciones_grupo_asignaturas()

    def on_pushButton_3(self):
            asig = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(asig)
            asig.exec_()

    def on_pushButton_4(self):
            asig = QtWidgets.QDialog()
            ui = Ui_DialogEscalafon()
            ui.setupUi(asig)
            asig.exec_()

    def on_pushButtonEstudiantes(self):
            asig = QtWidgets.QDialog()
            ui = Ui_DialogEstudiantes()
            ui.setupUi(asig,False)
            asig.exec_()

    def on_pushButton_7(self):
            asig = QtWidgets.QDialog()
            ui = Ui_DialogEstudiantes_suspensos()
            ui.setupUi(asig)
            asig.exec_()

    def on_pushButton_8(self):
            asig = QtWidgets.QDialog()
            ui = Ui_DialogEstudiantes_bajas()
            ui.setupUi(asig)
            asig.exec_()

    def on_pushButton_9(self):
            asig = QtWidgets.QDialog()
            ui = Ui_Dialog_Repitentes()
            ui.setupUi(asig)
            asig.exec_()

    def on_PushButtomCambiarCon(self):
            dialog = QtWidgets.QDialog()
            ui = Ui_CambiarContrasenna()
            ui.setupUi(dialog,False)
            dialog.exec_()
