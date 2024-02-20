% Carga el paquete de base de datos para Octave
pkg load database;

% Conexión a la base de datos (ajusta los parámetros según tu configuración)
conn = pq_connect(setdbopts('dbname', 'Parcial1', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', 'centenario'));

function menu()
    disp("1. Agregar nueva tarea");
    disp("2. Marcar tarea como completada");
    disp("3. Ver historial de tareas");
    disp("4. Borrar datos del usuario");
    disp("5. Regresar");
end

function usuario = ingresar_usuario()
    usuario = input("Ingrese su nombre de usuario: ", 's');
end

function usuario = registrar_usuario()
    usuario = input("Ingrese su nombre de usuario: ", 's');
    disp("Usuario registrado exitosamente.");
end

function agregar_tarea(usuario)
    tarea = input("Ingrese la descripción de la tarea: ", 's');
    fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ", 's');
    fecha_vencimiento = datestr(datenum(fecha_vencimiento), "YYYY-MM-DD");
end

function marcar_completada(usuario)
    tarea = input("Ingrese la descripción de la tarea que desea marcar como completada: ", 's');
    disp("La tarea ha sido marcada como completada.");
end

function ver_historial(usuario)
    disp("Aquí iría la consulta y el despliegue del historial de tareas.");
end

function borrar_datos_usuario(usuario)
    disp("Aquí iría la eliminación de los datos del usuario de la base de datos.");
end

function main()
    usuario = [];
    while true
        if isempty(usuario)
            disp("Por favor, ingrese o registre un usuario.");
            opcion = input("1. Ingresar\n2. Registrar\n3. Salir\nSeleccione una opción: ", 's');
            if opcion == "1"
                usuario = ingresar_usuario();
            elseif opcion == "2"
                usuario = registrar_usuario();
            elseif opcion == "3"
                break;
            else
                disp("Opción inválida. Por favor, seleccione nuevamente.");
            end
        else
            menu();
            opcion = input("Seleccione una opción: ", 's');

            if opcion == "1"
                agregar_tarea(usuario);
            elseif opcion == "2"
                marcar_completada(usuario);
            elseif opcion == "3"
                ver_historial(usuario);
            elseif opcion == "4"
                borrar_datos_usuario(usuario);
            elseif opcion == "5"
                usuario = [];
            else
                disp("Opción inválida. Por favor, seleccione nuevamente.");
            end
        end
    end
end

main();

