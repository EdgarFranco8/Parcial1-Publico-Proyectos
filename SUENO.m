pkg load database;

% Establecer conexión con la base de datos
conn = pq_connect(setdbopts('dbname', 'Parcial1', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', 'centenario'));

while true
    disp("1. Ingrese las horas de sueño diarias: ");
    disp("2. Salir");

    opcion = input("Seleccione una opción: ");

    switch opcion
      case 1
            % Agregar gasto realizado durante el viaje
            Usuario = input("Ingrese el nombre del usuario: ", 's');
            Fecha = input("Ingrese la fecha (YYYY-MM-DD): ", 's');
            Horas = input("Ingrese las horas que durmió en el dia: ");

            % Crear y ejecutar la consulta de inserción
            insert_query = sprintf("INSERT INTO Sueño (Usuario, Fecha, Horas) VALUES ('%s', '%s', %d);", Usuario, Fecha, Horas);
            pq_exec_params(conn, insert_query);

            disp("Control ingresado exitosamente.");

      case 2
             % Salir del programa
            pq_close(conn);
            disp("¡Hasta luego!");
            return;

        otherwise
            disp("Opción no válida. Por favor, seleccione una opción válida.");
    end
end
