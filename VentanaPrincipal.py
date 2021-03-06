# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WinMain(object):
    def setupUi(self, WinMain):
        WinMain.setObjectName("WinMain")
        WinMain.resize(974, 653)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        WinMain.setFont(font)
        self.centralwidget = QtWidgets.QWidget(WinMain)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.Flowsheet = QtWidgets.QGraphicsView(self.centralwidget)
        self.Flowsheet.setObjectName("Flowsheet")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Flowsheet)
        self.labelFeedback = QtWidgets.QTextEdit(self.centralwidget)
        self.labelFeedback.setMinimumSize(QtCore.QSize(0, 70))
        self.labelFeedback.setMaximumSize(QtCore.QSize(16777215, 70))
        self.labelFeedback.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.labelFeedback.setUndoRedoEnabled(False)
        self.labelFeedback.setReadOnly(True)
        self.labelFeedback.setMarkdown("")
        self.labelFeedback.setObjectName("labelFeedback")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelFeedback)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 100))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 644, 98))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Materia = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Materia.setMinimumSize(QtCore.QSize(70, 70))
        self.Materia.setMaximumSize(QtCore.QSize(70, 70))
        self.Materia.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Recursos/CDMIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Materia.setIcon(icon)
        self.Materia.setIconSize(QtCore.QSize(70, 70))
        self.Materia.setFlat(True)
        self.Materia.setObjectName("Materia")
        self.horizontalLayout.addWidget(self.Materia)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.scrollArea)
        WinMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WinMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuSimulaci_n = QtWidgets.QMenu(self.menubar)
        self.menuSimulaci_n.setObjectName("menuSimulaci_n")
        WinMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WinMain)
        self.statusbar.setObjectName("statusbar")
        WinMain.setStatusBar(self.statusbar)
        self.PropiedadesDock = QtWidgets.QDockWidget(WinMain)
        self.PropiedadesDock.setMinimumSize(QtCore.QSize(300, 167))
        self.PropiedadesDock.setAutoFillBackground(False)
        self.PropiedadesDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.PropiedadesDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.PropiedadesDock.setObjectName("PropiedadesDock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 282, 516))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setMinimumSize(QtCore.QSize(0, 15))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.txtNombre = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtNombre.setMinimumSize(QtCore.QSize(0, 20))
        self.txtNombre.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.verticalLayout.addWidget(self.txtNombre)
        self.gbInputs = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.gbInputs.setMinimumSize(QtCore.QSize(0, 130))
        self.gbInputs.setMaximumSize(QtCore.QSize(16777215, 130))
        self.gbInputs.setAlignment(QtCore.Qt.AlignCenter)
        self.gbInputs.setFlat(True)
        self.gbInputs.setObjectName("gbInputs")
        self.formLayout_3 = QtWidgets.QFormLayout(self.gbInputs)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.gbInputs)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cbInput2 = QtWidgets.QComboBox(self.gbInputs)
        self.cbInput2.setEnabled(False)
        self.cbInput2.setObjectName("cbInput2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbInput2)
        self.label_3 = QtWidgets.QLabel(self.gbInputs)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cbInput3 = QtWidgets.QComboBox(self.gbInputs)
        self.cbInput3.setEnabled(False)
        self.cbInput3.setObjectName("cbInput3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbInput3)
        self.label_4 = QtWidgets.QLabel(self.gbInputs)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.cbInput4 = QtWidgets.QComboBox(self.gbInputs)
        self.cbInput4.setEnabled(False)
        self.cbInput4.setObjectName("cbInput4")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cbInput4)
        self.cbInput1 = QtWidgets.QComboBox(self.gbInputs)
        self.cbInput1.setEnabled(False)
        self.cbInput1.setObjectName("cbInput1")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbInput1)
        self.label = QtWidgets.QLabel(self.gbInputs)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout.addWidget(self.gbInputs)
        self.gbOutputs = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.gbOutputs.setMinimumSize(QtCore.QSize(0, 130))
        self.gbOutputs.setMaximumSize(QtCore.QSize(16777215, 130))
        self.gbOutputs.setAlignment(QtCore.Qt.AlignCenter)
        self.gbOutputs.setFlat(True)
        self.gbOutputs.setCheckable(False)
        self.gbOutputs.setObjectName("gbOutputs")
        self.formLayout_2 = QtWidgets.QFormLayout(self.gbOutputs)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.gbOutputs)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cbOutput1 = QtWidgets.QComboBox(self.gbOutputs)
        self.cbOutput1.setEnabled(False)
        self.cbOutput1.setObjectName("cbOutput1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbOutput1)
        self.label_6 = QtWidgets.QLabel(self.gbOutputs)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.cbOutput2 = QtWidgets.QComboBox(self.gbOutputs)
        self.cbOutput2.setEnabled(False)
        self.cbOutput2.setObjectName("cbOutput2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbOutput2)
        self.label_7 = QtWidgets.QLabel(self.gbOutputs)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.cbOutput3 = QtWidgets.QComboBox(self.gbOutputs)
        self.cbOutput3.setEnabled(False)
        self.cbOutput3.setObjectName("cbOutput3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbOutput3)
        self.label_8 = QtWidgets.QLabel(self.gbOutputs)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.cbOutput4 = QtWidgets.QComboBox(self.gbOutputs)
        self.cbOutput4.setEnabled(False)
        self.cbOutput4.setObjectName("cbOutput4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cbOutput4)
        self.verticalLayout.addWidget(self.gbOutputs)
        self.groupBoxParametros = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBoxParametros.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxParametros.setFlat(True)
        self.groupBoxParametros.setCheckable(False)
        self.groupBoxParametros.setChecked(False)
        self.groupBoxParametros.setObjectName("groupBoxParametros")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBoxParametros)
        self.formLayout_4.setObjectName("formLayout_4")
        self.verticalLayout.addWidget(self.groupBoxParametros)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.groupBox = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lblAutor = QtWidgets.QLabel(self.groupBox)
        self.lblAutor.setText("")
        self.lblAutor.setObjectName("lblAutor")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblAutor)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lblVersion = QtWidgets.QLabel(self.groupBox)
        self.lblVersion.setText("")
        self.lblVersion.setObjectName("lblVersion")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblVersion)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.PropiedadesDock.setWidget(self.dockWidgetContents)
        WinMain.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.PropiedadesDock)
        self.actionNuevo = QtWidgets.QAction(WinMain)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionAbrir = QtWidgets.QAction(WinMain)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(WinMain)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_como = QtWidgets.QAction(WinMain)
        self.actionGuardar_como.setObjectName("actionGuardar_como")
        self.actionEjecutar = QtWidgets.QAction(WinMain)
        self.actionEjecutar.setObjectName("actionEjecutar")
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_como)
        self.menuSimulaci_n.addAction(self.actionEjecutar)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuSimulaci_n.menuAction())

        self.retranslateUi(WinMain)
        QtCore.QMetaObject.connectSlotsByName(WinMain)

    def retranslateUi(self, WinMain):
        _translate = QtCore.QCoreApplication.translate
        WinMain.setWindowTitle(_translate("WinMain", "MainWindow"))
        self.labelFeedback.setHtml(_translate("WinMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Medium\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.menuArchivo.setTitle(_translate("WinMain", "Archivo"))
        self.menuEditar.setTitle(_translate("WinMain", "Editar"))
        self.menuSimulaci_n.setTitle(_translate("WinMain", "Simulaci??n"))
        self.PropiedadesDock.setWindowTitle(_translate("WinMain", "Propiedades del bloque"))
        self.label_9.setText(_translate("WinMain", "Nombre"))
        self.gbInputs.setTitle(_translate("WinMain", "Inputs"))
        self.label_2.setText(_translate("WinMain", "Input 2:"))
        self.label_3.setText(_translate("WinMain", "Input 3:"))
        self.label_4.setText(_translate("WinMain", "Input 4:"))
        self.label.setText(_translate("WinMain", "Input 1:"))
        self.gbOutputs.setTitle(_translate("WinMain", "Outputs"))
        self.label_5.setText(_translate("WinMain", "Output 1:"))
        self.label_6.setText(_translate("WinMain", "Output 2:"))
        self.label_7.setText(_translate("WinMain", "Output 3:"))
        self.label_8.setText(_translate("WinMain", "Output 4:"))
        self.groupBoxParametros.setTitle(_translate("WinMain", "Par??metros"))
        self.label_10.setText(_translate("WinMain", "Autor:"))
        self.label_12.setText(_translate("WinMain", "Versi??n:"))
        self.actionNuevo.setText(_translate("WinMain", "Nuevo"))
        self.actionAbrir.setText(_translate("WinMain", "Abrir"))
        self.actionGuardar.setText(_translate("WinMain", "Guardar"))
        self.actionGuardar_como.setText(_translate("WinMain", "Guardar como"))
        self.actionEjecutar.setText(_translate("WinMain", "Ejecutar"))
        self.actionEjecutar.setShortcut(_translate("WinMain", "F5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WinMain = QtWidgets.QMainWindow()
    ui = Ui_WinMain()
    ui.setupUi(WinMain)
    WinMain.show()
    sys.exit(app.exec_())
