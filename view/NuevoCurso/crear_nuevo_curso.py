# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevo_curso.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from service.Curso_Service import Curso_Service
from PyQt5.QtWidgets import QDialog,QMessageBox


class Ui_Dialog_Nuevo_Curso(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(338, 273)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 113, 20))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(240, 50, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 321, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 311, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 301, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 220, 301, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 240, 321, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.spinBox.setValue(1)
        self.spinBox.setMinimum(1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(self.on_pushButton_2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Nuevo Curso"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "2020-2021"))
        self.label.setText(_translate("Dialog", "Nombre del nuevo curso"))
        self.label_2.setText(_translate("Dialog", "Cantidad de a??os"))
        self.pushButton.setText(_translate("Dialog", "Salir"))
        self.pushButton_2.setText(_translate("Dialog", "Crear"))
        self.label_3.setText(_translate("Dialog", "Nota: Los a??os y grupos se crear??n autom??ticamente  "))
        self.label_5.setText(_translate("Dialog", "y los alumnos ser??n insertados  en estos de forma"))
        self.label_6.setText(_translate("Dialog", "autom??tica. Si desea modificar alguna asignatura o"))
        self.label_7.setText(_translate("Dialog", "cambiar alg??n estudiante de grupo puede hacerlo "))
        self.label_8.setText(_translate("Dialog", "manualmente en sus respectivas interfaces"))


    def on_pushButton_2(self):
        if self.lineEdit.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("El curso debe tener un nombre")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            Curso_Service.iniciar_nuevo_curso(Curso_Service, self.lineEdit.text(), self.spinBox.value())
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Nuevo Curso creado correctamente")
            msg.setWindowTitle("Informaci??n")
            msg.exec_()