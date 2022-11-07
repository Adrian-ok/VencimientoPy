#-------------------------------------------------------------------------------#
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from BaseDatos.conexion import baseDatos
from herramientas.controlLogin import *
from PyQt5.QtCore import QDate
import datetime

#-------------------------------------------------------------------------------#
class controlMain():

    def __init__(self, fechaC, nroDias, vence, id_usuario, obs, nroT, cerrado, detalle, usuario, idrecor):
        self.fechaC = fechaC
        self.nroDias = nroDias
        self.vence = vence
        self.id_usuario = id_usuario
        self.obs = obs
        self.nroT = nroT
        self.cerrado = cerrado
        self.detalle = detalle

        self.usuario = usuario
        self.idrecor = idrecor

    def nuevoRecordatorio(self):

        self.fechaC = self.dateCarga.text()
        self.nroDias = self.txtDias.text()
        #------------------------------------------#
        f = self.dateVencimiento.selectedDate() #Guardo en f la fecha seleccionada en el calendario
        self.vence = f.toPyDate() #en f la fecha esta separada por comas y como entero, toPyDate() lo convierte a fecha separado con -
        #------------------------------------------#
        self.id_usuario = self.txtNroU.text()
        # self.obs = self.txtObs.toPlainText().upper()
        self.nroT = self.txtNroT.text()

        if self.checkBox.isChecked():
            self.cerrado = "0"
        else:
            self.cerrado = "1"

        self.obs = self.txtObs.text().upper()
        self.detalle = self.txtDetalle.text().upper()

        miCrud = baseDatos()
        
        if self.id_usuario == "" or self.nroDias == "" or self.obs == "" or self.detalle == "" or self.nroT == "":
            controlMain.Alert2(self, 0)
        else:
            if self.estado == "NUEVO":
                consulta = "INSERT INTO vencimientos(fechacarga, recordarxdias, vence, idusuario, obs, n_tramite, cerrado, detalle) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
                datos = (self.fechaC, self.nroDias, self.vence, self.id_usuario, self.obs, self.nroT, self.cerrado, self.detalle)
                miCrud.crearRecordatorio(consulta, (datos,))
                controlMain.Alert2(self, 1)

            if self.estado == "ACTUALIZAR":
                consulta = "UPDATE vencimientos SET idrecordatorio=%s, fechacarga=%s, recordarxdias=%s, vence=%s, idusuario=%s, obs=%s, n_tramite=%s, cerrado=%s, detalle=%s WHERE idrecordatorio=%s"
                datos = (self.idrecor, self.fechaC, self.nroDias, self.vence, self.id_usuario, self.obs, self.nroT, self.cerrado, self.detalle, self.selectedIdM)
                miCrud.updateRecord(consulta, (datos,))
                controlMain.Alert2(self, 2)
            
            self.dateCarga.clear()
            self.txtDias.clear()
            self.txtNroU.clear()
            self.txtObs.clear()
            self.txtNroT.clear()
            self.txtCerrado.clear()
            self.txtDetalle.clear()
            self.txtUser.clear()
            self.label_9.setText("Recordatorios")
            
            self.tablaVenci.setRowCount(0) #Seteo las filas de la tabla a 0, seria como vaciarla para que al volver a mostrarla no se dupliquen los datos
            user = control.usuarioId(self) #UsuarioId devuelve el nro de usruario que esta ocupando la app
            controlMain.tablaVencimientos(self, user) #LLamo a la tabla y le digo que me muestre los reg de user
            self.frame.hide()
            self.btnAnadir.show()
            self.btnEditar.show()
            self.estado = "DEFAULT"

    def tablaVencimientos(self, idusuario):
        miCrud = baseDatos()

        index = self.tablaVenci.rowCount()
        viejo = miCrud.Read(idusuario)

        for indice, ancho in enumerate((120, 115, 250,120,250), start=0):
            self.tablaVenci.setColumnWidth(indice, ancho)

        for row in viejo:
            self.tablaVenci.setRowCount(index + 1)
            # self.tablaVenci.setItem(index, 0, QTableWidgetItem(str(row[0])))#idrecordatorio
            self.tablaVenci.setItem(index, 0, QTableWidgetItem(str(row[0])))#fechacarga
            self.tablaVenci.setItem(index, 1, QTableWidgetItem(str(row[1])))#n_tramite
            self.tablaVenci.setItem(index, 2, QTableWidgetItem(str(row[3])))#obs
            self.tablaVenci.setItem(index, 3, QTableWidgetItem(str(row[2])))#vencimiento
            self.tablaVenci.setItem(index, 4, QTableWidgetItem(str(row[4])))#detalle
            
            index += 1


    def mostrarVencimientos(self):
        idUsuario = control.usuarioId(self)
        controlMain.tablaVencimientos(self, idUsuario)
 

    def ocultarFrame(self):

        self.frame.hide()
        self.frame2.hide()
        self.btnAnadir.show()
        self.btnEditar.show()
        self.label_9.setText("Recordatorios")

        self.dateCarga.clear()
        self.txtDias.clear()
        self.txtNroU.clear()
        self.txtObs.clear()
        self.txtNroT.clear()
        self.txtCerrado.clear()
        self.txtDetalle.clear()
        self.txtUser.clear()
        self.estafo = "DEFAULT"


    def mostrarFrame(self):
        self.frame.show()
        self.btnAnadir.hide()
        self.pushButton.setFocus()
        self.checkBox.setChecked(True)
        self.label_9.setText("Añadir Recordatorio")
        self.dateCarga.setDate(QtCore.QDate.currentDate())
        self.dateVencimiento.setSelectedDate(QtCore.QDate.currentDate())
        self.estado = "NUEVO"
        # self.frame.txtUser.setFocus()
        # self.dateVencimiento.setDate(QtCore.QDate.currentDate())

#-------------------------------------------------------------------------------#
#SELECCIONAR USUARIO

    def userSelect(self):

        self.frame2.show()
        self.btnAnadir.hide()
        self.pushButton.hide()
        self.tablaUsuarios.setRowCount(0)
        idUsuario = control.usuarioId(self)
        controlMain.tablaUsers(self, idUsuario)

    def tablaUsers(self, idu):
        miCrud = baseDatos()

        index = self.tablaUsuarios.rowCount()
        users = miCrud.readUser(idu)

        for row in users:
            self.tablaUsuarios.setRowCount(index + 1)
            self.tablaUsuarios.setItem(index, 0, QTableWidgetItem(str(row[0])))#idusuario
            self.tablaUsuarios.setItem(index, 1, QTableWidgetItem(str(row[1])))#ususario
            
            index += 1

    def cargarClickUser(self):
        miCrud = baseDatos()

        result = miCrud.userEspecifico(self.selectedId)

        for user in result:
            self.id_usuario = user[0]
            self.usuario = user[1]

        self.txtNroU.setText(str(self.id_usuario))
        self.txtUser.setText(self.usuario)

        self.frame2.hide()
        self.pushButton.show() 



    def doubleClickUser(self):
        item = self.tablaUsuarios.selectedItems()
        self.filaTabla = self.tablaUsuarios.currentRow()
        self.selectedId = int(item[0].text())
        print('itemm',int(item[0].text()))
        self.id_usuario = item[0].text()
        self.usuario = item[1].text()
        controlMain.cargarClickUser(self)

#-------------------------------------------------------------------------------#
#EDITAR

    def editSelected(self):
        self.frame.show()
        self.frame3.show()
        self.label_9.setText("Seleccione un Recordatorio")
        self.btnAnadir.hide()
        self.btnEditar.hide()
        self.tableWidget.setRowCount(0)
        self.estado = "ACTUALIZAR"
        idUsuario = control.usuarioId(self)
        controlMain.tablaEdit(self, idUsuario)

    def tablaEdit(self, idu):
        miCrud = baseDatos()

        index = self.tableWidget.rowCount()
        reg = miCrud.Read2(idu)

        for indice, ancho in enumerate((5, 100, 5,100,5, 250, 50, 1, 250), start=0):
            self.tableWidget.setColumnWidth(indice, ancho)

        for row in reg:
            self.tableWidget.setRowCount(index + 1)
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(row[0]))) #idrecordatorio
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(row[1]))) #fechacarga
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(row[2]))) #recordarxdias
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(index, 4, QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(index, 5, QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(index, 6, QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(index, 7, QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(index, 8, QTableWidgetItem(str(row[8])))

            index += 1

    def cargarEditar(self, idi):
        miCrud = baseDatos()

        result = miCrud.Read3(idi)

        for datos in result:
            self.idrecor = datos[0]
            self.fechaC = datos[1]
            self.nroDias = datos[2]
            self.vence = datos[3]
            self.idusuario = datos[4]
            self.obs = datos[5]
            self.n_tramite = datos[6]
            self.cerrado = datos[7]
            self.detalle = datos[3]

        self.txtNroU.setText(self.id_usuario)
        #-------------------------------------#
        #DATE-EDIT
        query = miCrud.obtenerNameUser(self.id_usuario)
        self.txtUser.setText(str(query[0][0]))
        #-------------------------------------#
        #DATA-LINE-EDIT
        fd = self.fechaC.replace('-',',')
        listaF = fd.split(',')
        date2 = QDate(int(listaF[0]), int(listaF[1]), int(listaF[2]))
        self.dateCarga.setDate(date2)

        #-------------------------------------#
        #CALENDARIO
        fc = self.vence.replace('-', ',')
        listaC = fc.split(',')
        date = QDate(int(listaC[0]), int(listaC[1]), int(listaC[2]))
        self.dateVencimiento.setSelectedDate(date)
        #-------------------------------------#
        self.txtDias.setText(self.nroDias)
        self.txtCerrado.setText(self.cerrado)
        self.txtObs.setText(self.obs)
        self.txtNroT.setText(self.nroT)
        self.txtDetalle.setText(self.detalle)

        if self.txtCerrado.text() == "0":
            self.checkBox.setChecked(True)

        self.frame3.hide()

    def doubleClickEditar(self):
        item = self.tableWidget.selectedItems()
        self.filaTabla = self.tableWidget.currentRow()
        self.selectedIdM = int(item[0].text())
        print('itemm',int(item[0].text()))
        self.idrecor = item[0].text()
        self.fechaC = item[1].text()
        self.nroDias = item[2].text()
        self.vence = item[3].text()
        self.id_usuario = item[4].text()
        self.obs = item[5].text()
        self.nroT = item[6].text()
        self.cerrado = item[7].text()
        self.detalle = item[8].text()
        controlMain.cargarEditar(self, self.idrecor)

#-------------------------------------------------------------------------------#
#ALERTAS

    def Alert2(self, nro):

        if nro == 0:
            return QMessageBox.critical(self.centralwidget, 'Error', "Asegurese de completar todos los campos", QMessageBox.Ok)
        elif nro == 1:
            return QMessageBox.information(self.centralwidget, 'Crear Recordatorio', "Recordatorio creado con exito", QMessageBox.Ok)
        elif nro == 2:
            return QMessageBox.information(self.centralwidget, 'Actualizar Recordatorio', "Recordatorio actualizado con exito", QMessageBox.Ok)

