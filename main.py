

# Menu 


# Data base
db = {}

salir = False




while not salir:     
    
    print("""
        1) Nueva Contraseña   
        2) Mostrar Contraseña
        3) Actualizar Contraseña
        4) Escribe "Salir" para salir del programa
        """)
    menu = input('Selecciona el numero de la operacion que vayas a realizar: ')



    # Introducir nuevas contraseñas
    if menu == "1":

        idenfiticador = input('Introduce la URL:  ')
        valor = input('Introduce la contraseña:  ')

        if idenfiticador not in db:
            db[idenfiticador] = valor
        else:
            print('Esa contraseña ya existe')    
        print(db)
    # Mostrar contraseñas
    elif menu == "2":
            
        print(db.keys())
        idenfiticador = input('¿Que contraseña quieres mostrar? ')

        if idenfiticador not in db:
            print('Esa contraseña no existe')
        else:
            print(f'la contrasña es {db[idenfiticador]}')
            salir = True
    # Actualizar contraseña
    elif menu == "3":

        print(db.keys())
        password = input('Cual es la contraseña que quieres actualizar: ')
        update = input('Escribe la nueva contraseña: ')
        db[password] = update

    elif menu in ["Salir","salir"]:
        salir = True
            
    
    print('Fin')    


    