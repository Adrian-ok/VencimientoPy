from email.mime import base
from PyQt5.QtWidgets import QMessageBox
from BaseDatos.conexion import baseDatos
from PyQt5 import QtWidgets

usuario = []
idUsuario = 0

class control():

    def __init__(self, usuario, contra):
        self.usuario = usuario
        self.contra = contra

    def iniciarSesion(self, vent_abrir, vent_cerrar): #le paso los parametros de ventana cerrar y abrir

        miBD = baseDatos()

        self.usuario = str("'" + self.txtUsuario.text() + "'") #le agrego las comillas para que la funcione la consulta
        self.contra = str("'" + self.txtContra.text() + "'")

        dato1 = miBD.buscarUsuario(self.usuario) #guardo el resultado de la consulta en dato (devuelve una lista con tuplas)
        dato2 = miBD.buscarContra(self.contra)

        if dato1 == [] and dato2 == []: # dato1 y dato2 == vacio -> usuario y contraseña Incorrectos
            control.Alert(self, 0)
        else:
            if dato1 == []:
                control.Alert(self, 1) # dato1 == vacio -> usuario Incorrecto 
            else:
                usuario.append(dato1[0][0])
                print("esto es usuario de controlLogin:", usuario)
                print("")


            if dato2 == []:
                control.Alert(self, 2) # dato2 == vacio -> contraseña Incorrecta
            else:
                pass

            if dato1 != [] and dato2 !=[]: 
                vent_cerrar.hide(self) # ventana cerrar == al login pantalla que ejecuto como main y la paso como paramtro al cliquear btn iniciar sesion
                self.ventana2 = QtWidgets.QMainWindow() 
                self.ui = vent_abrir() 
                self.ui.setupUi(self.ventana2)
                self.ventana2.show()
        
        return idUsuario

    def usuarioId(self):
        idUsuario = usuario[0]
        return idUsuario

    def Alert(self, nro):

        if nro == 0:
            msgIncorrecto = QMessageBox.warning(self, 'Inicio de sesion', "Usuario y Contraseña incorrectos", QMessageBox.Ok)
            return msgIncorrecto
        elif nro == 1:
            msgUsuario = QMessageBox.warning(self, 'Inicio de sesion', "Usuario incorrecto", QMessageBox.Ok)
            return msgUsuario
        elif nro == 2:
            msgContra = QMessageBox.warning(self, 'Inicio de sesion', "Contraseña incorrecta", QMessageBox.Ok)
            return msgContra


        


