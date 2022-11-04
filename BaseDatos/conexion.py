import mysql.connector

class baseDatos():

    def __init__(self):
        self.conexion = mysql.connector.connect(host = 'localhost',
                                                port = '3306',
                                                database = 'ejemplo1',
                                                user = 'root',
                                                password = '0303')

    def crearUsuario(self, consulta, datos):
        cursor = self.conexion.cursor()
        cursor.executemany(consulta, datos)
        self.conexion.commit()
        cursor.close()
        self.conexion.close()

    def crearRecordatorio(self, consulta, datos):
        cursor = self.conexion.cursor()
        cursor.executemany(consulta, datos)
        self.conexion.commit()
        cursor.close()
        self.conexion.close()

    def updateRecord(self, consulta, datos):
        cursor = self.conexion.cursor()
        cursor.executemany(consulta, datos)
        self.conexion.commit()
        cursor.close()
        self.conexion.close()

    def buscarUsuario(self, user):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM usuarios WHERE usuario = {};".format(user)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def buscarContra(self, contra):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM usuarios WHERE contrasena = {};".format(contra)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def verificacion(self, user, contra):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM usuarios WHERE usuario = {} AND contrasena = {};".format(user, contra)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def Read(self, idu):
        cursor = self.conexion.cursor()
        sql = "SELECT CONVERT(fechacarga, CHAR), n_tramite, CONVERT(vence, CHAR), obs, detalle FROM vencimientos WHERE idusuario = {} AND cerrado = {}".format(idu, 0)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def Read2(self, idu):
        cursor = self.conexion.cursor()
        sql = "SELECT idrecordatorio, CONVERT(fechacarga, CHAR), recordarxdias, CONVERT(vence, CHAR), idusuario, obs, n_tramite, cerrado, detalle FROM vencimientos WHERE idusuario = {} AND cerrado = {}".format(idu, 0)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def Read3(self, idu):
        cursor = self.conexion.cursor()
        sql = "SELECT idrecordatorio, CONVERT(fechacarga, INT), recordarxdias, vence, obs, n_tramite, cerrado, detalle FROM vencimientos WHERE idusuario = {}".format(idu)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def readUser(self, idu):
        cursor = self.conexion.cursor()
        sql = "SELECT idusuario, usuario FROM usuarios WHERE idusuario <> {}".format(idu)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def userEspecifico(self, idu):
        cursor = self.conexion.cursor()
        sql = "SELECT idusuario, usuario FROM usuarios WHERE idusuario = {}".format(idu)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def obtenerNameUser(self, idu):
        cursor = self.conexion.cursor()
        sql = "SELECT usuario FROM usuarios WHERE idusuario = {}".format(idu)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result