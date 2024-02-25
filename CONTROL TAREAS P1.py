import psycopg2
from datetime import datetime

# Conexión a la base de datos
conn = psycopg2.connect(
    dbname="Parcial1",
    user="postgres",
    password="centenario",
    host="localhost"
)


def ingresar_usuario():
    usuario = input("Por favor, introduzca su nombre de usuario: ")
    # Insertar usuario en la base de datos si no existe
    with conn.cursor() as cursor:
        cursor.execute("SELECT Usuario FROM Ejercicios WHERE Usuario = %s", (usuario,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO Ejercicios (Usuario, Rutina, Tiempo, Calorias) VALUES (%s, %s, %s, %s)", (usuario, "", "", None, 0, 0))
            conn.commit()
            print("Usuario registrado exitosamente.")
        else:
            print("Bienvenido de vuelta,", usuario)
    return usuario


def menu():
    print("1. Agregar nuevo ejercicio")
    print("2. Ver el historial de ejercicios")
    print("4. Eliminar todos los datos del usuario")
    print("5. Salir del sistema")


def agregar_libro(usuario):
    libro = input("Por favor, introduzca el nombre del libr: ")
    autor = input("Por favor, introduzca el nombre del autor: ")
    fecha = input("Por favor, introduzca la fecha de lectura (YYYY-MM-DD): ")
    fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
    paginas_leidas = int(input("Por favor, introduzca la cantidad de páginas leídas: "))
    meta_paginas = int(input("Por favor, introduzca la meta de páginas para la próxima lectura: "))
    # Insertar libro en la base de datos
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO Lectura (Usuario, Libro, Autor, Fecha, Paginas_leidas, Meta_paginas) VALUES (%s, %s, %s, %s, %s, %s)", (usuario, libro, autor, fecha, paginas_leidas, meta_paginas))
        conn.commit()



def ver_historial(usuario):
    # Obtener historial de libros leídos del usuario
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Lectura WHERE Usuario = %s", (usuario,))
        libros = cursor.fetchall()
        for libro in libros:
            estado = "Completado" if libro[7] else "Pendiente"
            print(f"ID: {libro[0]}, Libro: {libro[2]}, Autor: {libro[3]}, Fecha: {libro[4]}, Páginas leídas: {libro[5]}, Meta de páginas: {libro[6]}, Estado: {estado}")


def borrar_datos_usuario(usuario):
    # Borrar todos los libros del usuario de la base de datos
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM Lectura WHERE Usuario = %s", (usuario,))
        conn.commit()
    print("Todos los datos del usuario han sido eliminados.")


def recomendaciones(usuario):
    titulo_libro = input("Por favor, introduzca el título del libro que desea recomendar: ")
    print(f"Gracias por tu recomendación, {usuario}! Has sugerido el libro: {titulo_libro}")


def main():
    usuario = ingresar_usuario()
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro(usuario)
        elif opcion == "2":
            ver_historial(usuario)
        elif opcion == "3":
            recomendaciones(usuario)
        elif opcion == "4":
            borrar_datos_usuario(usuario)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


if __name__ == "__main__":
    main()