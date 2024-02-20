% Carga el paquete de base de datos para Octave
pkg load database;

% Conexión a la base de datos (ajusta los parámetros según tu configuración)
conn = pq_connect(setdbopts('dbname', 'Parcial1', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', 'centenario'));

while true
    % Mostrar menú
    disp("1. Registrar libro leído: ");
    disp("2. Establecer meta de lectura: ");
    disp("3. Salir");

    % Solicitar opción al usuario
    opcion = input("Seleccione una opción: ");

    switch opcion
        case 1
% Agregar libro
            Usuario = input("Ingrese el nombre del usuario: ", 's');
            Libro = input("Ingrese el titulo del libro leido: ", 's');
            Autor = input("Ingrese el nombre del autor del libro: ", 's');
            Fecha = input("Ingrese la fecha de lectura (YYYY-MM-DD): ", 's');
            Paginas_leidas = input("Ingrese el numero de paginas leidas: ");
            Meta_paginas = input("Ingrese la meta de paginas a leer: ");


            % Crear y ejecutar la consulta de inserción
            insert_query = sprintf("INSERT INTO Lectura (Usuario, Libro, Autor, Fecha, Paginas_leidas, Meta_paginas) VALUES ('%s', '%s', '%s', '%s', %d, %d);", Usuario, Libro, Autor, Fecha, Paginas_leidas, Meta_paginas);
            pq_exec_params(conn, insert_query);

            disp("Libro registrado exitosamente.");

        case 2
            Usuario = input("Ingrese el nombre de usuario: ", 's');
            Meta_paginas = input("Ingrese la meta de paginas a leer: ");

            establecer_meta_lectura(conn, usuario, meta_paginas);
            disp('Meta de lectura establecida correctamente.');

        case 3
             % Salir del programa
            pq_close(conn);
            disp("¡Hasta luego!");
            return;

        otherwise
            disp("Opción no válida. Por favor, seleccione una opción válida.");
    end


end
