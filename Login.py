import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from herramientas.controlLogin import control
from MainWindow import Ui_MainWindow


class Login(QMainWindow):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        loadUi("Login.ui", self)

        self.txtUsuario.setFocus()
        self.btnLogin.clicked.connect(lambda: control.iniciarSesion(self, Ui_MainWindow, Login))
        # self.btnLogin.returnPressed.connect(lambda: control.iniciarSesion(self, Ui_MainWindow, Login))
        self.txtUsuario.returnPressed.connect(lambda: self.txtContra.setFocus())
        self.txtContra.returnPressed.connect(lambda: self.btnLogin.setFocus())

if __name__ == "__main__":
    mi_aplicacion = QApplication(sys.argv)
    mi_app = Login()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
