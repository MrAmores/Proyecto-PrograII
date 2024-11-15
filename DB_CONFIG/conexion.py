import mysql.connector

def conexionDB():
    conexion = mysql.connector.connect(
    host= 'localhost',
    user ='root',
    password = 'esteban2511',
    port= '3306',
    database= 'crucero'
    ) 
    return conexion
