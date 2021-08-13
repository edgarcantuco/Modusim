# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SplashScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WinSplash(object):
    def setupUi(self, WinSplash):
        WinSplash.setObjectName("WinSplash")
        WinSplash.setWindowModality(QtCore.Qt.ApplicationModal)
        WinSplash.resize(800, 600)
        WinSplash.setMinimumSize(QtCore.QSize(800, 600))
        WinSplash.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        WinSplash.setFont(font)
        WinSplash.setWindowTitle("")
        WinSplash.setWindowOpacity(0.95)
        self.centralwidget = QtWidgets.QWidget(WinSplash)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.btnNuevo = QtWidgets.QPushButton(self.centralwidget)
        self.btnNuevo.setGeometry(QtCore.QRect(10, 350, 380, 40))
        self.btnNuevo.setObjectName("btnNuevo")
        self.btnArchivo1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnArchivo1.setGeometry(QtCore.QRect(410, 350, 380, 40))
        self.btnArchivo1.setObjectName("btnArchivo1")
        self.btnAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbrir.setGeometry(QtCore.QRect(10, 410, 380, 40))
        self.btnAbrir.setObjectName("btnAbrir")
        self.btnArchivo2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnArchivo2.setGeometry(QtCore.QRect(410, 410, 380, 40))
        self.btnArchivo2.setObjectName("btnArchivo2")
        self.btnArchivo3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnArchivo3.setGeometry(QtCore.QRect(410, 470, 380, 40))
        self.btnArchivo3.setObjectName("btnArchivo3")
        self.btnArchivo4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnArchivo4.setGeometry(QtCore.QRect(410, 530, 380, 40))
        self.btnArchivo4.setObjectName("btnArchivo4")
        self.btnAyuda = QtWidgets.QPushButton(self.centralwidget)
        self.btnAyuda.setGeometry(QtCore.QRect(10, 470, 380, 40))
        self.btnAyuda.setObjectName("btnAyuda")
        self.btnCerrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCerrar.setGeometry(QtCore.QRect(10, 530, 380, 40))
        self.btnCerrar.setObjectName("btnCerrar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 580, 201, 20))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        WinSplash.setCentralWidget(self.centralwidget)

        self.retranslateUi(WinSplash)
        QtCore.QMetaObject.connectSlotsByName(WinSplash)

    def retranslateUi(self, WinSplash):
        _translate = QtCore.QCoreApplication.translate
        self.btnNuevo.setText(_translate("WinSplash", "Crear nueva simulación"))
        self.btnArchivo1.setText(_translate("WinSplash", "Archivo-1"))
        self.btnAbrir.setText(_translate("WinSplash", "Abrir simulación"))
        self.btnArchivo2.setText(_translate("WinSplash", "Archivo-2"))
        self.btnArchivo3.setText(_translate("WinSplash", "Archivo-3"))
        self.btnArchivo4.setText(_translate("WinSplash", "Archivo-4"))
        self.btnAyuda.setText(_translate("WinSplash", "Ayuda"))
        self.btnCerrar.setText(_translate("WinSplash", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WinSplash = QtWidgets.QMainWindow()
    ui = Ui_WinSplash()
    ui.setupUi(WinSplash)
    WinSplash.show()
    sys.exit(app.exec_())