pkg load database; % Carga el paquete necesario para la conexión a la base de datos

% Establecer la conexión a la base de datos
conn = pq_connect(setdbopts('dbname', 'Parcial1', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', 'centenario'));

% Menú de opciones para el usuario
opcion = 0;
while opcion ~= 4
    disp('Menú:');
    disp('1. Registrar gasto en alimentos');
    disp('2. Analizar hábitos alimenticios');
    disp('3. Establecer metas nutricionales');
    disp('4. Salir');

    opcion = input('Seleccione una opción: ');

    switch opcion
        case 1
            % Registro de gasto en alimentos
            usuario = input('Ingrese el nombre del usuario: ', 's');
            alimento = input('Ingrese el nombre del alimento: ', 's');
            cantidad = input('Ingrese la cantidad: ');
            costo = input('Ingrese el precio: ');

            % Insertar el registro en la base de datos
            insert_query = sprintf("INSERT INTO gastos (usuario, alimento, cantidad, costo) VALUES ('%s','%s', %f, %f)", usuario, alimento, cantidad, costo);
            exec(conn, insert_query); % Ejecutar la consulta utilizando la función exec
            disp('Gasto registrado exitosamente');
        case 2
            % Análisis de hábitos alimenticios (puedes implementar análisis aquí)
            disp('Análisis de hábitos alimenticios');
            % Aquí puedes agregar código para analizar los datos de gastos en alimentos
        case 3
            % Establecer metas nutricionales (puedes implementar esta funcionalidad aquí)
            disp('Establecer metas nutricionales');
            % Aquí puedes agregar código para establecer metas nutricionales
        case 4
            disp('Saliendo del programa...');
        otherwise
            disp('Opción no válida');
    end
end

% Cerrar la conexión a la base de datos al salir del programa
close(conn);


