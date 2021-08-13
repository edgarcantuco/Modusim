from PyQt5 import QtCore, QtGui, QtWidgets

from SplashScreen import Ui_WinSplash
from VentanaPrincipal import Ui_WinMain
import os
from xml.dom import minidom


class Splash(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_WinSplash()
        self.ui.setupUi(self)
        
        QtWidgets.QMainWindow.setWindowFlags(self, QtCore.Qt.FramelessWindowHint)

        self.ui.btnNuevo.clicked.connect(self.Nuevo)
        self.ui.btnCerrar.clicked.connect(self.Cerrar)

    def Nuevo(self):
        self.ui.label.setText('Preparando la simulación')
        self.widget_Principal = Principal()
        self.ui.label.setText('Cargando módulos')
        self.widget_Principal.CargarModulos()
        self.hide()
        self.widget_Principal.showMaximized()

    def Cerrar(self):
        self.close()



class Principal(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_WinMain()
        self.ui.setupUi(self)

        self.ui.PropiedadesDock.hide()
        self.PrepararEscena()

        self.seleccionado = 0
        self.ui.Flowsheet.mousePressEvent = self.FlowsheetPresionado

        self.bloquesagregados = []

        self.ui.labelFeedback.textCursor().blockFormat().setLineHeight(500, QtGui.QTextBlockFormat.ProportionalHeight)
        self.ui.labelFeedback.textCursor().clearSelection()
        self.ui.Flowsheet.scene().selectionChanged.connect(self.CambioSeleccion)

        self.lblParametros = []
        self.WidgetParametros = []

    ## Preparación flowsheet y agregar bloques al diagrama

    def PrepararEscena(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.ui.Flowsheet.width(), self.ui.Flowsheet.height())
        self.gris = QtGui.QBrush(QtCore.Qt.darkGray)
        self.pen = QtGui.QPen(QtCore.Qt.black)
        self.ui.Flowsheet.setScene(self.scene)
        self.ui.Flowsheet.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

    def AgregarBloqueUsuario(self):
        sender = self.sender()
        self.seleccionado = self.modulos.index(sender.objectName()) + 1
        cursor_pix = self.imagenes[self.seleccionado - 1]
        cursor_pix = QtGui.QCursor(cursor_pix, -1, -1)
        self.setCursor(cursor_pix)
        self.ui.statusbar.showMessage("Módulo " + sender.objectName() + " seleccionado. Presione una parte del diagrama de flujo para agregarlo.")

    def FlowsheetPresionado(self, event):
        super(QtWidgets.QGraphicsView, self.ui.Flowsheet).mousePressEvent(event)
        if event.button() != QtCore.Qt.LeftButton:
            return

        if event.modifiers() & QtCore.Qt.ControlModifier:
            event.ignore()

        if not self.seleccionado == 0:
            self.bloquesagregados.append(self.scene.addPixmap(self.imagenes[self.seleccionado - 1]))
            self.bloquesagregados[-1].setFlags(QtWidgets.QGraphicsItem.ItemIsMovable | QtWidgets.QGraphicsItem.ItemIsSelectable)
            self.bloquesagregados[-1].setPos(event.x() - 50, event.y() - 50)
            self.bloquesagregados[-1].index = len(self.bloquesagregados)
            self.bloquesagregados[-1].indexPar = self.seleccionado
            self.bloquesagregados[-1].Parametros = []
            self.bloquesagregados[-1].Nombre = ""

            n = 1

            for x in self.bloquesagregados:
                if x.Nombre == self.informacionBloque[x.indexPar - 1]["Info"]["Nombre"] + str(n):
                    n += 1
                else:
                    self.bloquesagregados[-1].Nombre = self.informacionBloque[x.indexPar - 1]["Info"]["Nombre"] + str(n)
            
            for x in self.informacionBloque[self.bloquesagregados[-1].indexPar - 1]["Parametros"]:
                self.bloquesagregados[-1].Parametros.append(x["Default"])

            self.seleccionado = 0
            self.ui.statusbar.showMessage("")
            self.setCursor(QtCore.Qt.ArrowCursor)

    ## Cargar bloques seleccionados en el dock

    def CambioSeleccion(self):
        if len(self.ui.Flowsheet.scene().selectedItems()) > 0:
            self.DockShown(True)
            self.CargarDock(self.ui.Flowsheet.scene().selectedItems()[0].index, self.ui.Flowsheet.scene().selectedItems()[0].indexPar)
        else:
            self.DockShown(False)

    def DockShown(self, Visible):
        if Visible == True:
            self.ui.PropiedadesDock.show()
        else:
            self.ui.PropiedadesDock.hide()

    def CargarDock(self, index, indexPar):
        parametros = self.informacionBloque[indexPar - 1]
        self.ui.lblAutor.setText(parametros["Info"]["Autor"])
        self.ui.lblVersion.setText(parametros["Info"]["Version"])
        self.ui.txtNombre.setText(self.bloquesagregados[index - 1].Nombre)

        inputs = []
        inputs.append(self.ui.cbInput1)
        inputs.append(self.ui.cbInput2)
        inputs.append(self.ui.cbInput3)
        inputs.append(self.ui.cbInput4)

        outputs = []
        outputs.append(self.ui.cbOutput1)
        outputs.append(self.ui.cbOutput2)
        outputs.append(self.ui.cbOutput3)
        outputs.append(self.ui.cbOutput4)

        if parametros["Config"]["LimInputs"]:
            if int(parametros["Config"]["NumInputs"]) < 4:
                for x in range(int(parametros["Config"]["NumInputs"])):
                    inputs[x].setEnabled(True)
            else:
                for x in range(4):
                    inputs[x].setEnabled(True)
                self.ImprimirFeedback("El número de inputs en el archivo Parámetros.xml del bloque " + self.modulos[indexPar - 1] + " es mayor al número máximo de inputs (4), por lo tanto, se configuró con 4 inputs.", 1)

        if parametros["Config"]["LimOutputs"]:
            if int(parametros["Config"]["NumOutputs"]) < 4:
                for x in range(int(parametros["Config"]["NumOutputs"])):
                    outputs[x].setEnabled(True)
            else:
                for x in range(4):
                    outputs[x].setEnabled(True)
                self.ImprimirFeedback("El número de outputs en el archivo Parámetros.xml del bloque es mayor al número máximo de outputs (4), por lo tanto, se configuró con 4 outputs.", 1)

        for x in self.lblParametros:
            self.ui.formLayout_4.removeWidget(x)
        for x in self.WidgetParametros:
            self.ui.formLayout_4.removeWidget(x)

        self.lblParametros = []
        self.WidgetParametros = []
        
        for x in range(len(parametros["Parametros"])):
            self.lblParametros.append(QtWidgets.QLabel(self.ui.groupBoxParametros))
            self.lblParametros[-1].setText(parametros["Parametros"][x]["Label"])
            self.lblParametros[-1].wordWrap = True
            self.ui.formLayout_4.setWidget(x*2, QtWidgets.QFormLayout.FieldRole, self.lblParametros[-1])

            Tipo = parametros["Parametros"][x]["Tipo"]
            if Tipo == "Textbox":
                self.AgregarTextbox(x, index, self.bloquesagregados[index - 1].Parametros[x])
            elif Tipo == "Slider":
                self.AgregarSlider(x, index, parametros["Parametros"][x]["Min"], parametros["Parametros"][x]["Max"], self.bloquesagregados[index - 1].Parametros[x], parametros["Parametros"][x]["Step"])
            elif Tipo == "ComboBox":
                self.AgregarCombobox(x, index, self.bloquesagregados[index - 1].Parametros[x], parametros["Parametros"][x]["Opciones"])
            elif Tipo == "Botón":
                self.AgregarBoton(x, index, parametros["Parametros"][x]["Texto"], parametros["Parametros"][x]["Funcion"])

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui.formLayout_4.addItem(spacerItem)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout.addItem(spacerItem)

    ## Textbox

    def AgregarTextbox(self, x, index, Valor):
        self.WidgetParametros.append(QtWidgets.QLineEdit(self.ui.groupBoxParametros))
        self.WidgetParametros[-1].setText(Valor)
        self.WidgetParametros[-1].setValidator(QtGui.QDoubleValidator())
        self.ui.formLayout_4.setWidget(x*2 + 1, QtWidgets.QFormLayout.FieldRole, self.WidgetParametros[-1])
        self.WidgetParametros[-1].x = x
        self.WidgetParametros[-1].index = index
        self.WidgetParametros[-1].textChanged.connect(self.keyEnter)

    def keyEnter(self):
        self.bloquesagregados[self.sender().index - 1].Parametros[self.sender().x] = self.sender().text()

    ## Slider

    def AgregarSlider(self, x, index, Min, Max, Valor, Step):
        self.WidgetParametros.append(QtWidgets.QSlider(self.ui.groupBoxParametros))
        self.WidgetParametros[-1].setOrientation(QtCore.Qt.Horizontal)
        self.WidgetParametros[-1].setMinimum(0)
        self.WidgetParametros[-1].setMaximum(int((float(Max) - float(Min)) / float(Step)))
        self.WidgetParametros[-1].setValue(int((float(Valor) / float(Step)) + float(Min)))
        self.ui.formLayout_4.setWidget(x*2 + 1, QtWidgets.QFormLayout.FieldRole, self.WidgetParametros[-1])
        self.WidgetParametros[-1].Min = float(Min)
        self.WidgetParametros[-1].Max = float(Max)
        self.WidgetParametros[-1].Step = float(Step)
        self.WidgetParametros[-1].x = x
        self.WidgetParametros[-1].index = index
        self.WidgetParametros[-1].valueChanged.connect(self.CambioSlider)

    def CambioSlider(self):
        self.bloquesagregados[self.sender().index - 1].Parametros[self.sender().x] = (self.sender().value() - self.sender().Min) * self.sender().Step

    ## Combobox

    def AgregarCombobox(self, x, index, Valor, Opciones):
        self.WidgetParametros.append(QtWidgets.QComboBox(self.ui.groupBoxParametros))
        self.ui.formLayout_4.setWidget(x*2 + 1, QtWidgets.QFormLayout.FieldRole, self.WidgetParametros[-1])
        self.WidgetParametros[-1].currentIndexChanged.connect(self.CambioCB)
        self.WidgetParametros[-1].x = x
        self.WidgetParametros[-1].index = index
        listOpciones = Opciones.split(", ")

        for n in listOpciones:
            self.WidgetParametros[-1].addItem(n)

        self.WidgetParametros[-1].setCurrentIndex(int(Valor) - 1)

    def CambioCB(self):
        self.bloquesagregados[self.sender().index - 1].Parametros[self.sender().x] = self.sender().currentIndex() + 1

    ## Botón

    def AgregarBoton(self, x, index, texto, fun):
        self.WidgetParametros.append(QtWidgets.QPushButton(self.ui.groupBoxParametros))
        self.ui.formLayout_4.setWidget(x*2 + 1, QtWidgets.QFormLayout.FieldRole, self.WidgetParametros[-1])
        self.WidgetParametros[-1].setText(texto)
        self.WidgetParametros[-1].x = x
        self.WidgetParametros[-1].index = index
        self.WidgetParametros[-1].fun = fun
        self.WidgetParametros[-1].clicked.connect(self.BtnClick)

    def BtnClick(self):
        respuesta = self.funciones[self.sender().index - 1][self.sender().x].Main()
        if "Feedback" in respuesta.keys():
            self.ImprimirFeedback(respuesta["Feedback"], 4)
        self.bloquesagregados[self.sender().index - 1].Parametros[self.sender().x] = respuesta["Parámetro"]

    ## Feedback

    def ImprimirFeedback(self, Feedback, tipo):
        
        ## TIPOS 
        # 1: Advertencia
        # 2: Error
        # 3: Correcto
        # 4: Mensaje de usuario 

        if tipo == 1:
            texto = "•<font color=gold> Advertencia: <\font> <font color=black>"
        elif tipo == 2:
            texto = "•<font color=red> Error: <\font> <font color=black>"
        elif tipo == 3:
            texto = "•<font color=green> Exito: <\font> <font color=black>"
        else:
            texto = "•"

        self.ui.labelFeedback.append('<span style=" font-size:10pt;">' + texto + Feedback + "<\font><\span>")
        self.ui.labelFeedback.moveCursor(QtGui.QTextCursor.End)
        self.ui.labelFeedback.ensureCursorVisible()

    ## Cargar módulos

    def CargarModulos(self):

        cwd = os.getcwd()

        bloqueusuario = []
        self.bloque = []
        self.modulos = []
        self.imagenes = []
        self.informacionBloque = []
        self.funciones = []

        for folder in os.listdir(cwd + '\Modulos'):

            if os.path.exists(cwd + '\Modulos\ '[:-1] + folder + '\ '[:-1] + folder + ".py"):

                importar = True
                feedback = "No se pudo importar el módulo <html><b>" + folder + "</b></html>. Problemas:"

                try:
                    bloqueTemporal = __import__('Modulos.' + folder + '.' + folder, fromlist=["Main"])
                except:
                    feedback += " •El código del archivo principal no está contenido dentro de una función Main."
                    importar = False

                try:
                    if os.path.exists(cwd + '\Modulos\ '[:-1] + folder + '\Icono.png'):
                        icon = QtGui.QIcon()
                        iconoTemporal = QtGui.QPixmap(cwd + '\Modulos\ '[:-1] + folder + '\Icono.png')
                    else:
                        importar = False
                        feedback += " •El archivo Icono.png no existe."
                except:
                    feedback += " •No se pudo cargar el ícono del bloque."
                    importar = False

                try:
                    docxml = minidom.parse(cwd + '\Modulos\ '[:-1] + folder + '\Parametros.xml')
                    info = {"Nombre":  (docxml.getElementsByTagName('Nombre'))[0].firstChild.data, "Autor": (docxml.getElementsByTagName('Autor'))[0].firstChild.data, "Version": (docxml.getElementsByTagName('Versión'))[0].firstChild.data}
                    config = {"LimInputs": (docxml.getElementsByTagName('LimitarInputs'))[0].firstChild.data, "LimOutputs": (docxml.getElementsByTagName('LimitarOutputs'))[0].firstChild.data, "NumInputs": (docxml.getElementsByTagName('NumInputs'))[0].firstChild.data, "NumOutputs": (docxml.getElementsByTagName('NumOutputs'))[0].firstChild.data}
                    par = docxml.getElementsByTagName('Parametro')

                    parametros = []

                    for item in par:
                        dictParametros = dict(item.attributes.items())
                        parametros.append(dictParametros)
                except:
                    feedback += " •No existe el archivo Parametros.xml o está mal configurado."
                    importar = False

                if importar:

                        funcionestemporales = []
                        for x in parametros:
                            if "Funcion" in x.keys():
                                try:
                                    funcionestemporales.append(__import__('Modulos.' + folder + '.' + 'Funciones.' + x["Funcion"], fromlist=["Main"]))
                                except:
                                    importar = False
                                    feedback += " •No se pudo importar la función " + x["Funcion"]
                            else:
                                funcionestemporales.append(0)

            else:
                importar = False
                feedback = "No se pudo importar el módulo <html><b>" + folder + "</b></html>. Problemas:"
                feedback += " •El archivo de Python principal tiene que tener el mismo nombre que la carpeta."

            if importar:
                self.bloque.append(bloqueTemporal)
                bloqueusuario.append(QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents))
                bloqueusuario[-1].setMinimumSize(QtCore.QSize(70, 70))
                bloqueusuario[-1].setMaximumSize(QtCore.QSize(70, 70))
                bloqueusuario[-1].setText("")
                bloqueusuario[-1].setFlat(True)

                self.imagenes.append(iconoTemporal)
                icon.addPixmap(self.imagenes[-1], QtGui.QIcon.Normal, QtGui.QIcon.Off)
                bloqueusuario[-1].setIcon(icon)
                bloqueusuario[-1].setIconSize(QtCore.QSize(70, 70))

                bloqueusuario[-1].setObjectName(folder)
                self.modulos.append(bloqueusuario[-1].objectName())
                self.ui.horizontalLayout.addWidget(bloqueusuario[-1])
                bloqueusuario[-1].clicked.connect(self.AgregarBloqueUsuario)

                self.informacionBloque.append({"Info": info, "Config": config, "Parametros": parametros})

                self.funciones.append(funcionestemporales)

                self.ImprimirFeedback("El módulo " + folder + " fue importado correctamente.", 3)
                
            else:
                self.ImprimirFeedback(feedback, 1)

        del bloqueTemporal
        del iconoTemporal
        del info
        del config
        del parametros

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ui.horizontalLayout.addItem(spacerItem)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget_Splash = Splash()
    widget_Splash.show()

    app.exec_()