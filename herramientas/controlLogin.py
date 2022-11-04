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
        dato3 = miBD.verificacion(self.usuario, self.contra)


        if dato1 != [] and dato2 != []:
            if dato1 == []:
                control.Alert(self, 1) #Usuario incorrecto 
                usuario.clear() #vacio lista contenedora del id
            else:
                usuario.append(dato1[0][0])#cargo id usuario para ocupar despues 
                print("usuario" , usuario)
                if dato2 == []:
                    control.Alert(self, 2)#Contraseña incorrecta
                else:
                    if dato3 == []:
                        control.Alert(self, 0)#usuario y contraseña incorrectos
                        usuario.clear()
                    else:
                        vent_cerrar.hide(self) # ventana cerrar == al login pantalla que ejecuto como main y la paso como paramtro al cliquear btn iniciar sesion
                        self.ventana2 = QtWidgets.QMainWindow() 
                        self.ui = vent_abrir() 
                        self.ui.setupUi(self.ventana2)
                        self.ventana2.show()
        else:
            control.Alert(self, 0)
            usuario.clear()   

        # return idUsuario

    def usuarioId(self):
        idUsuario = usuario[0]
        return idUsuario

    def Alert(self, nro):

        if nro == 0:
            msgIncorrecto = QMessageBox.warning(self, 'Inicio de sesion', "Usuario y contraseña Incorrectos", QMessageBox.Ok)
            return msgIncorrecto
        elif nro == 1:
            msgUsuario = QMessageBox.warning(self, 'Inicio de sesion', "Usuario incorrecto", QMessageBox.Ok)
            return msgUsuario
        elif nro == 2:
            msgContra = QMessageBox.warning(self, 'Inicio de sesion', "Contraseña incorrecta", QMessageBox.Ok)
            return msgContra




        


