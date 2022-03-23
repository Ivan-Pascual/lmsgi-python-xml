import mysql.connector

def conexion():
    mydb = mysql.connector.connect(
    host="192.168.8.19",
    user="admin",
    password="admin",
    )
    return mydb



def ver():
    mibasedatos = conexion().cursor()
    mibasedatos.execute("Show databases")
    for x in mibasedatos:
        print(x)