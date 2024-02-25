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
    with conn.cursor() as cursor:
        cursor.execute("SELECT Usuario FROM gestionV WHERE Usuario = %s", (usuario,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO gestionV (Usuario, Alojamiento, Transporte, Alimentacion) VALUES (%s, %s, %s, %s)", (usuario, 0, 0, 0))
            conn.commit()
            print("Usuario registrado exitosamente.")
        else:
            print("Bienvenido de vuelta,", usuario)
    return usuario


def menu():
    print("1. Agregar un gasto en el viaje")
    print("2. Ver el historial de gastos en el viaje")
    print("3. Eliminar un gasto del viaje")
    print("4. Salir del sistema")


def agregar_gasto_viaje(usuario):
    alojamiento = float(input("Introduzca el gasto de alojamiento: "))
    transporte = float(input("Introduzca el gasto de transporte: "))
    alimentacion = float(input("Introduzca el gasto de alimentación: "))
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO gestionV (Usuario, Alojamiento, Transporte, Alimentacion) VALUES (%s, %s, %s, %s)", (usuario, alojamiento, transporte, alimentacion))
        conn.commit()


def ver_historial_gastos(usuario):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM gestionV WHERE Usuario = %s", (usuario,))
        gastos = cursor.fetchall()
        for gasto in gastos:
            print(f"ID: {gasto[0]}, Alojamiento: {gasto[1]}, Transporte: {gasto[2]}, Alimentación: {gasto[3]}")


def eliminar_gasto_viaje(usuario):
    # Borrar todos los libros del usuario de la base de datos
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM gestionV WHERE Usuario = %s", (usuario,))
        conn.commit()
    print("Todos los datos del usuario han sido eliminados.")


# Resto de las funciones no modificadas


def main():
    usuario = ingresar_usuario()
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_gasto_viaje(usuario)
        elif opcion == "2":
            ver_historial_gastos(usuario)
        elif opcion == "3":
            eliminar_gasto_viaje(usuario)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


if __name__ == "__main__":
    main()
