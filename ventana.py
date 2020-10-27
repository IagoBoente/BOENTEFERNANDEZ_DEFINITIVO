# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(658, 389)
        self.centralwidget = QtWidgets.QWidget(venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lblXexCli = QtWidgets.QLabel(self.centralwidget)
        self.lblXexCli.setGeometry(QtCore.QRect(250, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblXexCli.setFont(font)
        self.lblXexCli.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.46, y1:0.0343636, x2:0.4595, y2:0.835, stop:0 rgba(0, 223, 185, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:rgb(56, 56, 56)")
        self.lblXexCli.setTextFormat(QtCore.Qt.RichText)
        self.lblXexCli.setAlignment(QtCore.Qt.AlignCenter)
        self.lblXexCli.setObjectName("lblXexCli")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 40, 591, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(30, 70, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 140, 591, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.editDni = QtWidgets.QLineEdit(self.centralwidget)
        self.editDni.setGeometry(QtCore.QRect(90, 60, 141, 20))
        self.editDni.setObjectName("editDni")
        self.lblApel = QtWidgets.QLabel(self.centralwidget)
        self.lblApel.setGeometry(QtCore.QRect(30, 100, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblApel.setFont(font)
        self.lblApel.setObjectName("lblApel")
        self.editApel = QtWidgets.QLineEdit(self.centralwidget)
        self.editApel.setGeometry(QtCore.QRect(90, 100, 251, 20))
        self.editApel.setObjectName("editApel")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(360, 100, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.editNome = QtWidgets.QLineEdit(self.centralwidget)
        self.editNome.setGeometry(QtCore.QRect(420, 100, 201, 20))
        self.editNome.setObjectName("editNome")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(250, 170, 71, 21))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(350, 170, 71, 21))
        self.btnSalir.setObjectName("btnSalir")
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(venPrincipal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArchivo = QtWidgets.QMenu(self.menuBar)
        self.menuArchivo.setObjectName("menuArchivo")
        venPrincipal.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuBar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(venPrincipal)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "Proyecto Uno"))
        self.lblXexCli.setText(_translate("venPrincipal", "XESTIÓN CLIENTES"))
        self.lblDNI.setText(_translate("venPrincipal", "DNI: "))
        self.lblApel.setText(_translate("venPrincipal", "Apellidos: "))
        self.lblNome.setText(_translate("venPrincipal", "Nombre: "))
        self.btnAceptar.setText(_translate("venPrincipal", "Aceptar"))
        self.btnSalir.setText(_translate("venPrincipal", "Salir"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
        self.actionSalir.setShortcut(_translate("venPrincipal", "Alt+S"))
