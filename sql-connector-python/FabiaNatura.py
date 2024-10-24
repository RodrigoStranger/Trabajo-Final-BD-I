import mysql.connector



config = { 'user': 'rodrigo', 'password': 'ubnt', 'host': 'localhost', 'database': 'FabiaNatura', 'port': 3306 } 

conexion = mysql.connector.connect(**config)

#cursor = conexion.cursor()

#crear_bd = '''

#'''

#cursor.execute(crear_bd)

#conexion.commit()
#cursor.close()
conexion.close()