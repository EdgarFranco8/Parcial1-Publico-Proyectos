pkg load database;

% Establecer conexión con la base de datos
conn = pq_connect(setdbopts('dbname', 'Parcial1', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', 'centenario'));

while true
    disp("1. Ingrese el gasto realizado: ");
    disp("2. Eliminar gasto: ");
    disp("3. Ver historial de gastos realizados: ");
    disp("4. Salir");

    opcion = input("Seleccione una opción: ");

    switch opcion

        case 1
            % Agregar gasto realizado durante el viaje
            Usuario = input("Ingrese el nombre del usuario: ", 's');
            Alojamiento = input("Ingrese el gasto realizado en alojamiento: ");
            Transporte = input("Ingrese el gasto realizado en transporte: ");
            Alimentacion = input("Ingrese el gasto realizado en alimentacion: ");

            % Crear y ejecutar la consulta de inserción
            insert_query = sprintf("INSERT INTO gestionV (Usuario, Alojamiento, Transporte, Alimentacion) VALUES ('%s', %f, %f, %f);", Usuario, Alojamiento, Transporte, Alimentacion);
            pq_exec_params(conn, insert_query);

            disp("Gasto ingresado exitosamente.");

        case 2
            % Eliminar un gasto de la base de datos
            UsuarioEliminar = input("Ingrese el nombre del usuario a eliminar: ", 's');

            % Crear y ejecutar la consulta de eliminación
            delete_query = sprintf("DELETE FROM gestionV WHERE Usuario = '%s';", UsuarioEliminar);
            pq_exec_params(conn, delete_query);

            disp("Gasto eliminado exitosamente.");

        case 3
            % Ver historial de gastos
   select_all_query = "SELECT * FROM gestionV;";
            result = pq_exec_params(conn, select_all_query);

            disp("Historial de gastos:");

            % Iterar sobre los resultados y mostrarlos
            while result.next()
                Usuario = result.getString(1);
                Alojamiento = result.getDouble(2);
                Transporte = result.getDouble(3);
                Alimentacion = result.getDouble(4);

                fprintf("Usuario: %s, Alojamiento: %f, Transporte: %f, Alimentacion: %f\n", Usuario, Alojamiento, Transporte, Alimentacion);
            end

        case 4
            % Salir del programa
            pq_close(conn);
            disp("¡Hasta luego!");
            return;

        otherwise
            disp("Opción no válida. Por favor, seleccione una opción válida.");
    end
end







