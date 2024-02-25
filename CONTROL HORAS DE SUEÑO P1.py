import psycopg2
import matplotlib.pyplot as plt
import numpy as np

# Conectar a la base de datos PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="centenario",
    database="Parcial1",
    port="5432"
)


# Función para insertar un registro de sueño
# Función para insertar un registro de sueño
def insert_Sueno(Usuario, Fecha, Horas):
    # Crear un cursor a partir de la conexión
    cursor = conn.cursor()
    # Ejecutar la consulta SQL para insertar un registro de sueño
    cursor.execute("INSERT INTO Sueno (Usuario, Fecha, Horas) VALUES (%s, %s, %s)", (Usuario, Fecha, Horas))
    # Confirmar la operación
    conn.commit()
    # Cerrar el cursor
    cursor.close()


# Función para obtener todos los registros de sueño de un nombre
# Función para obtener todos los registros de sueño de un usuario
def get_sleep(Usuario):
    # Crear un cursor a partir de la conexión
    cursor = conn.cursor()
    # Ejecutar la consulta SQL para obtener los registros de sueño
    cursor.execute("SELECT * FROM Sueno WHERE Usuario = %s", (Usuario,))
    # Obtener todos los registros y devolverlos
    sleep_records = cursor.fetchall()
    # Cerrar el cursor
    cursor.close()
    return sleep_records


# Función para obtener el promedio de horas de sueño por día de la semana de un nombre
# Función para obtener el promedio de horas de sueño por día de la semana de un usuario
def get_sleep_average_by_weekday(Usuario):
    # Crear un cursor a partir de la conexión
    cursor = conn.cursor()
    # Ejecutar la consulta SQL para obtener el promedio de horas de sueño por día de la semana
    cursor.execute("SELECT EXTRACT(DOW FROM Fecha) AS weekday, AVG(Horas) AS average FROM Sueno WHERE Usuario = %s GROUP BY weekday ORDER BY weekday", (Usuario,))
    # Obtener todos los registros y devolverlos
    sleep_average = cursor.fetchall()
    # Cerrar el cursor
    cursor.close()
    return sleep_average


# Función para mostrar un gráfico de barras con el promedio de horas de sueño por día de la semana
def plot_sleep_average_by_weekday(data):
    weekdays = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    x = [weekdays[int(row[0])] for row in data]
    y = [row[1] for row in data]
    plt.bar(x, y, color="green")
    plt.xlabel("Día de la semana")
    plt.ylabel("Promedio de horas de sueño")
    plt.title("Análisis de patrón de sueño")
    plt.show()

# Función para ofrecer dos sugerencias para mejorar la calidad de descanso
def suggest_sleep_improvement(data):
    # Define weekdays
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Calculate the overall average of sleep hours
    total_average = np.mean([row[1] for row in data])
    # Calculate the day of the week with fewer sleep hours
    min_day = min(data, key=lambda row: row[1])
    # Calculate the day of the week with more sleep hours
    max_day = max(data, key=lambda row: row[1])
    # Initialize the suggestions
    suggestions = []
    # If the overall average is less than 7 hours, suggest sleeping more
    if total_average < 7:
        suggestions.append(f"You should sleep more hours in general. The recommended average is at least 7 hours per night. Your current average is {total_average:.2f} hours.")
    # If the day with fewer sleep hours is very different from the day with more hours, suggest having a more regular schedule
    if abs(min_day[1] - max_day[1]) > 2:
        suggestions.append(f"You should have a more regular sleep schedule. Sleeping much more or much less some days can affect your circadian rhythm. Your day with fewer sleep hours is the {weekdays[int(min_day[0])]}, with {min_day[1]:.2f} hours. Your day with more sleep hours is the {weekdays[int(max_day[0])]}, with {max_day[1]:.2f} hours.")
    # If there are no suggestions, congratulate for the good sleep habit
    if not suggestions:
        suggestions.append("Congratulations! You have a good sleep habit. Keep it up.")
    # Return the suggestions
    return suggestions

# Función para mostrar el menú interactivo
def show_menu():
    print("Bienvenido al programa de registro y análisis de sueño.")
    print("Selecciona una opción:")
    print("1. Registrar horas de sueño")
    print("2. Ver registros de sueño")
    print("3. Ver análisis de patrón de sueño")
    print("4. Ver sugerencias para mejorar la calidad de descanso")
    print("5. Salir")

# Función para validar la entrada del usuario
def validate_input(prompt, type, min=None, max=None):
    while True:
        try:
            value = type(input(prompt))
            if min is not None and value < min:
                raise ValueError(f"El valor debe ser mayor o igual a {min}")
            if max is not None and value > max:
                raise ValueError(f"El valor debe ser menor o igual a {max}")
            return value
        except ValueError as e:
            print(f"Entrada inválida: {e}")

# Función principal
def main():
    # Obtener el nombre del usuario
    name = input("Ingrese el nombre del usuario: ")
    # Mostrar el menú interactivo
    show_menu()
    # Obtener la opción del usuario
    option = validate_input("Elija una opcion: ", int, 1, 5)
    # Repetir hasta que el usuario elija salir
    while option != 5:
        # Ejecutar la opción elegida
        if option == 1:
            # Registrar horas de sueño
            date = input("Fecha a registrar? (AAAA-MM-DD): ")
            hours = validate_input("¿Cuántas horas dormiste?: ", float, 0)
            insert_Sueno(name, date, hours)
            print("Registro guardado con éxito.")
        elif option == 2:
            # Ver registros de sueño
            sleep_data = get_sleep(name)
            if sleep_data:
                print("Estos son tus registros de sueño:")
                for row in sleep_data:
                    print(f"Fecha: {row[1]}, Horas: {row[2]}")
            else:
                print("No tienes registros de sueño.")
        elif option == 3:
            # Ver análisis de patrón de sueño
            sleep_average = get_sleep_average_by_weekday(name)
            if sleep_average:
                print("Este es tu análisis de patrón de sueño:")
                plot_sleep_average_by_weekday(sleep_average)
            else:
                print("No tienes suficientes datos para el análisis.")
        elif option == 4:
            # Ver sugerencias para mejorar la calidad de descanso
            sleep_average = get_sleep_average_by_weekday(name)
            if sleep_average:
                print("Estas son tus sugerencias para mejorar la calidad de descanso:")
                sleep_suggestions = suggest_sleep_improvement(sleep_average)
                for suggestion in sleep_suggestions:
                    print(f"- {suggestion}")
            else:
                print("No tienes suficientes datos para las sugerencias.")
        # Mostrar el menú interactivo de nuevo
        show_menu()
        # Obtener la opción del usuario de nuevo
        option = validate_input("¿Qué opción eliges? ", int, 1, 5)
    # Despedirse del usuario
    print("Gracias por usar el programa. ¡Hasta pronto!")

# Ejecutar la función principal
if __name__ == "__main__":
    main()