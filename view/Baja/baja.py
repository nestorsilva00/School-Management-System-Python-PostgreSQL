# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baja.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from service.Baja_Service import Baja_Service
from service.Motivo_Baja_Service import Motivo_Baja_Service


class Ui_dlgBaja(object):
    def setupUi(self, dlgReportes, cod_estudiante, isBaja):
        self.d = dlgReportes
        self.cod_estudiante = cod_estudiante
        self.isBaja  = isBaja
        dlgReportes.setObjectName("dlgReportes")
        dlgReportes.resize(361, 169)
        dlgReportes.setStyleSheet("QLabel{\n"
"background-color: rgb(51, 103, 145);\n"
"border-radius:12px;\n"
"}\n"
"QPushButton{\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(112, 112, 112);\n"
"border-right:2px solid rgb(170, 170, 170);\n"
"border-bottom:2px solid rgb(170, 170, 170);\n"
"}\n"
"QPushButton:hover{\n"
"border-right:1px solid rgb(170, 170, 170);\n"
"border-bottom:1px solid rgb(170, 170, 170)\n"
"}\n"
"QPushButton:pressed{\n"
"border:0px;\n"
"}\n"
"QComboBox{\n"
"border-radius:12px;\n"
"}\n"
"")
        self.comboBox = QtWidgets.QComboBox(dlgReportes)
        self.comboBox.setGeometry(QtCore.QRect(40, 80, 281, 21))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.comboBox.setObjectName("comboBox")
        self.btnCancelar = QtWidgets.QPushButton(dlgReportes)
        self.btnCancelar.setGeometry(QtCore.QRect(10, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet("background-color: rgb(255, 21, 21);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnAceptar = QtWidgets.QPushButton(dlgReportes)
        self.btnAceptar.setGeometry(QtCore.QRect(270, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setObjectName("btnAceptar")
        self.label_2 = QtWidgets.QLabel(dlgReportes)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 361, 121))
        self.label_2.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(dlgReportes)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(dlgReportes)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 341, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btnCancelar.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        self.btnAceptar.raise_()
        self.label_3.raise_()
        self.retranslateUi(dlgReportes)
        QtCore.QMetaObject.connectSlotsByName(dlgReportes)

        # ----------
        self.cargar_motivos()
        self.btnAceptar.clicked.connect(self.on_btnAceptar_clicked)
        self.btnCancelar.clicked.connect(self.d.close)
        if(isBaja):
           self.label_3.setVisible(True)
        else:
           self.label_3.setVisible(False)

    def retranslateUi(self, dlgReportes):
        _translate = QtCore.QCoreApplication.translate
        dlgReportes.setWindowTitle(_translate("dlgReportes", "Baja"))
        self.btnCancelar.setText(_translate("dlgReportes", "Cancelar"))
        self.btnAceptar.setText(_translate("dlgReportes", "Aceptar"))
        self.label.setText(_translate("dlgReportes", "Seleccione un motivo"))
        self.label_3.setText(_translate("dlgReportes", "El estudiante ya es baja,puedes eliminar la baja o cambiar el motivo"))

    def cargar_motivos(self):
            motivos = Motivo_Baja_Service.read_motivo_baja(Motivo_Baja_Service)
            if(self.isBaja):
                self.comboBox.addItem("Eliminar baja")
                for i in motivos:
                    self.comboBox.addItem(i.get_motivo())
            else:
                for i in motivos:
                    self.comboBox.addItem(i.get_motivo())

    def on_btnAceptar_clicked(self):
            if not self.isBaja:
                cod_motivo = Motivo_Baja_Service.get_codMotivo_dado_motivo(Motivo_Baja_Service, self.comboBox.currentText())
                Baja_Service.create_baja(Baja_Service, self.cod_estudiante, cod_motivo)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Baja realizada satisfactoriamente")
                msg.setWindowTitle("Baja satisfactoria")
                msg.exec()
                self.d.close()
            else:
                if self.comboBox.currentText() == "Eliminar baja" :
                    Baja_Service.delete_baja(Baja_Service,self.cod_estudiante)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Baja eliminada satisfactoriamente")
                    msg.setWindowTitle("Baja eliminada")
                    msg.exec()
                    self.d.close()
                else:
                    cod_motivo = Motivo_Baja_Service.get_codMotivo_dado_motivo(Motivo_Baja_Service, self.comboBox.currentText())
                    Baja_Service.update_baja(Baja_Service,cod_motivo,self.cod_estudiante)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Baja modificada satisfactoriamente")
                    msg.setWindowTitle("Baja modificada")
                    msg.exec()
                    self.d.close()











