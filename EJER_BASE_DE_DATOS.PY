import sqlite3
conexion=sqlite3.connect("guardar_heroes.db")
cursor=conexion.cursor()  
cursor.execute("""
CREATE TABLE IF NOT EXISTS heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rol TEXT, #El text es un tipo de dato que guarda palabras o frases, ideal para el nombre y el rol.
    nivel INTEGER #El integer es un tipo de dato que guarda números enteros, ideal para el nivel
    )
""")
while True:
    print("¿Quieres crear un nuevo personaje? (s/n)")
    respuesta=input().lower() #el lower() convierte la respuesta a minúscula para evitar errores de mayúsculas
    if respuesta=="s":
        print("Bienvenido a la creación de tu personaje")
        nombre=input("Define el nombre de tu personaje")
        rol=input("Define el rol de tu personaje")
        nivel=int(input("Define el nivel de tu personaje"))
        cursor.execute("INSERT INTO heroes (nombre, rol, nivel) VALUES (?, ?, ?)", (nombre, rol, nivel))
        conexion.commit() 
    else:
        break

cursor.execute("SELECT * FROM heroes")
filas=cursor.fetchall()
print("--- REGISTROS EN LA BASE DE DATOS ---")
for fila in filas:
    print(fila)
conexion.close()