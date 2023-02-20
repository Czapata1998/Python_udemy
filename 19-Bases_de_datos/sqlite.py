#Importar modulo
import sqlite3

#Conexion

conexion = sqlite3.connect('pruebas.db')

#Crear un cursor

cursor = conexion.cursor()


#Crear una tabla

''' cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo VARCHAR(255), "+
"descripcion TEXT, "+
"precio INT(255)"+
")") '''

''' cursor.execute("""
CREATE TABLE IF NOT EXISTS productos("+
id INTEGER PRIMARY KEY AUTOINCREMENT, 
titulo VARCHAR(255), 
descripcion TEXT, 
precio INT(255)
);
""") '''

#Guardar cambios
conexion.commit()

#Insertar datos

''' cursor.execute("INSERT INTO productos VALUES (null, 'primer producto', 'descripcion de ni producto', 90)")
conexion.commit() '''

#Borrar registros

cursor.execute("DELETE FROM productos")
conexion.commit()

#Insertar muchos registros de golpe

productos = [
    ("Ordenador portatil", "Buen pc", 700),
    ("Telefono", "Buen movil", 800),
    ("televisor", "Buen televisor", 500),
    ("dvd", "Buen dvd", 200),
    ("nevera", "Buena nevera", 300),
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()
#Update
cursor.execute("UPDATE productos SET precio=799 WHERE precio=800 ")


#Listar datos de la tabla

cursor.execute("SELECT * FROM productos WHERE precio >= 400;") #Where solo saca los productos que cumplan la condicion
productos = cursor.fetchall()

for producto in productos:
    print("ID:", producto[0])
    print("Titulo:", producto[1])
    print("Descripcion:", producto[2])
    print("Precio:", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone() #Para sacar el primer registro de mi tabla
print(producto)
#Cerrar la conexion

conexion.close()