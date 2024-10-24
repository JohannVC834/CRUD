import mysql.connector

# Conexión a la base de datos
database = mysql.connector.connect(
    host='localhost',           # localhost para conexión local
    user='root',                # Cambia 'root' por tu usuario de MySQL
    password='',                # Cambia por tu contraseña, si es que tienes
    database='crud' # Reemplaza 'tu_base_de_datos' con el nombre de tu base de datos
)

# Verificación de conexión
if database.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error en la conexión a la base de datos")
