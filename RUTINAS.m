pkg load database

% Establecer la conexión a la base de datos
conn = pq_connect(setdbopts('dbname', 'Parcial1', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', 'centenario'));

while true
    % Mostrar menú
    disp("1. Agregar rutina");
    disp("2. Eliminar rutina");
    disp("3. Ver lista de rutinas");
    disp("4. Salir");

    % Solicitar opción al usuario
    opcion = input("Seleccione una opción: ");

    switch opcion
        case 1
            % Agregar estudiante
            Usuario = input("Ingrese el nombre del usuario: ", 's');
            Rutina = input("Ingrese la rutina realizada: ", 's');
            Tiempo = input("Ingrese el tiempo empleado en minutos: ");
            Fecha = input("Ingrese la fecha de la rutina (YYYY-MM-DD): ", 's')

            % Crear y ejecutar la consulta de inserción
            insert_query = sprintf("INSERT INTO Fisicos (Usuario, Rutina, Tiempo, Fecha) VALUES ('%s', '%s', %d, '%s');", Usuario, Rutina, Tiempo, Fecha);
            pq_exec_params(conn, insert_query);

            disp("Rutina agregada exitosamente.");

        case 2
             % Eliminar un gasto de la base de datos
            UsuarioEliminar = input("Ingrese el nombre del usuario a eliminar: ", 's');

            % Crear y ejecutar la consulta de eliminación
            delete_query = sprintf("DELETE FROM Fisicos WHERE Usuario = '%s';", UsuarioEliminar);
            pq_exec_params(conn, delete_query);

            disp("Rutina eliminada exitosamente.");

        case 3
             % Ver lista de estudiantes
            select_all_query = "SELECT * FROM Fisicos;";
            result = pq_exec_params(conn, select_all_query);

            disp("Lista de rutinas:");
            disp(result.data);

       case 4
             % Salir del programa
            pq_close(conn);
            disp("¡Hasta luego!");
            return;

        otherwise
            disp("Opción no válida. Por favor, seleccione una opción válida.");
    end
end



