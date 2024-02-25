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
        cursor.execute("SELECT Usuario FROM GastosAlimenticios WHERE Usuario = %s", (usuario,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO GastosAlimenticios (Usuario, Alimento, Cantidad, Costo) VALUES (%s, %s, %s, %s)", (usuario, "", 0, 0))
            conn.commit()
            print("Usuario registrado exitosamente.")
        else:
            print("Bienvenido de vuelta,", usuario)
    return usuario


def menu():
    print("1. Agregar gastos alimenticios")
    print("2. Análisis de hábitos alimenticios")
    print("3. Ajustar presupuesto")
    print("4. Establecer metas nutricionales")
    print("5. Eliminar todos los datos del usuario")
    print("6. Salir del sistema")


def agregar_gasto_alimenticio(usuario):
    alimento = input("Por favor, introduzca el alimento comprado: ")
    cantidad = float(input("Por favor, introduzca la cantidad de alimento comprado: "))
    costo = float(input("Por favor, introduzca el costo de la compra: "))
    # Insertar gasto alimenticio en la base de datos
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO GastosAlimenticios (Usuario, Alimento, Cantidad, Costo) VALUES (%s, %s, %s, %s)", (usuario, alimento, cantidad, costo))
        conn.commit()


def analisis_habitos_alimenticios(usuario):
    # Realizar análisis de hábitos alimenticios del usuario
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM GastosAlimenticios WHERE Usuario = %s", (usuario,))
        gastos = cursor.fetchall()
        total_gastado = sum(gasto[3] for gasto in gastos)
        print(f"Total gastado en alimentos: ${total_gastado}")


def ajustar_presupuesto(usuario):
    # Realizar ajustes de presupuesto según los hábitos alimenticios del usuario
    print("¡Funcionalidad de ajuste de presupuesto aún no implementada!")


def establecer_metas_nutricionales(usuario):
    # Establecer metas nutricionales para el usuario
    print("¡Funcionalidad de establecimiento de metas nutricionales aún no implementada!")


def borrar_datos_usuario(usuario):
    # Borrar todas las tareas y gastos alimenticios del usuario de la base de datos
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM Alimenticios WHERE Usuario = %s", (usuario,))
        conn.commit()
    print("Todos los datos del usuario han sido eliminados.")


def main():
    usuario = ingresar_usuario()
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_gasto_alimenticio(usuario)
        elif opcion == "2":
            analisis_habitos_alimenticios(usuario)
        elif opcion == "3":
            ajustar_presupuesto(usuario)
        elif opcion == "4":
            establecer_metas_nutricionales(usuario)
        elif opcion == "5":
            borrar_datos_usuario(usuario)
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


if __name__ == "__main__":
    main()