#---------------------------------------------------------------------#
#IMPORTACIONES
import configparser, mysql.connector
from datetime import date
import datetime
from notifypy import Notify

#---------------------------------------------------------------------#
#CONEXION
conexion = mysql.connector.connect(host = 'localhost',
                                   port = '3306',
                                   database = 'ejemplo1',
                                   user = 'root',
                                   password = '0303')
#---------------------------------------------------------------------#
#PROGRAMACION

def obtenerDatos(idu):
    cursor = conexion.cursor()
    sql = "SELECT recordarxdias, CONVERT(vence, CHAR) FROM vencimientos WHERE idusuario = {} AND cerrado = {}".format(idu, 0)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conexion.close()
    return result

def notificacion(cant):
    notification = Notify()
    notification.title = "Vencimiento"
    notification.message = f"Se detectaron {cant} Vencimientos"
    notification.icon = "img/fecha-de-vencimiento.png"
    
    return notification.send()


def funcion(list):
    cantV = 0
    hoy = date.today()
    for i in range(len(list)):
        d = 0
        v = 1
        dia = list[i][d]
        vence = list[i][v]

        fecha = hoy + datetime.timedelta(days = dia)

        if str(fecha) >= vence:
            cantV = cantV + 1 

    if cantV > 0:
        notificacion(cantV)

# ---------------------------------------------------------------------#
config = configparser.ConfigParser()
config.read('Settings.dat')
usuario = (config['Usuarios']['usuario'])

resultados=obtenerDatos(usuario)
funcion(resultados)

