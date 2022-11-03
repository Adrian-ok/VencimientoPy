from PyQt5 import QtCore, QtGui, QtWidgets
from herramientas.controlLogin import control



class Ui_RegistrarC(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 358)
        MainWindow.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"background-color: rgb(170, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(70, 70, 311, 31))
        self.txtUsuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtContra = QtWidgets.QLineEdit(self.centralwidget)
        self.txtContra.setGeometry(QtCore.QRect(70, 160, 311, 31))
        self.txtContra.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtContra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtContra.setObjectName("txtContra")
        self.btnGuarC = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuarC.setGeometry(QtCore.QRect(60, 240, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuarC.setFont(font)
        self.btnGuarC.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnGuarC.setObjectName("btnGuarC")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnGuarC.clicked.connect(lambda: control.crearCuenta(self))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Usuario:"))
        self.label_2.setText(_translate("MainWindow", "Contraseña:"))
        self.btnGuarC.setText(_translate("MainWindow", "GUARDAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RegistrarC()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
