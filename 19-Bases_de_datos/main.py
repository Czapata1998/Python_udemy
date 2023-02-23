import mysql.connector  #py -m pip install mysql-connector-python --extension que funciono

# Conexion a la base de datos
database = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database = "master_python"
    )

# ejecutar consultas, cursor 

cursor = database.cursor(buffered=True)

# Crear base de datos
''' cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd) '''
    
    
#Crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")


''' cursor.execute("SHOW TABLES")

for table in cursor:
    print(table) '''
    
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")

coches = [
    ('Seat', 'Ibiza', 5000 ),
    ('Reanult', 'Clio', 15000 ),
    ('Citroen', 'Saxo', 2000 ),
    ('Mercedes', 'Clase c', 35000 ),
    ('Chevrolet', 'Camaro', 65000 )
]

cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches) # insertar de forma masiva
database.commit() #para que se guarden los cambios

#Listar
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")  #cONSULTAR TODOS LOS DATOS QUE TENGO EN LA BASE

result = cursor.fetchall()


print("------ TODOS MIS COCHES---")
for coche in result:
    print(coche[1], coche[2], coche [3])


cursor.execute("SELECT * FROM vehiculos")  #cONSULTAR TODOS LOS DATOS QUE TENGO EN LA BASE

coche = cursor.fetchone() #Sacar el primer dato de la tasbla 

print(coche)

# Borrar  
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes' ") 

database.commit()

print(cursor.rowcount, "borrados!!")

#Actualizar

cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat' ")

database.commit()

print(cursor.rowcount, "Actualizados!!")

