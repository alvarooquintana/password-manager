from tinydb import TinyDB, Query

 


# Data base

database = TinyDB('db.json')

#db = {}

salir = False


selector = Query()

while not salir:     
    
    print("""
        1) Nueva Contraseña   
        2) Mostrar Contraseña
        3) Actualizar Contraseña
        4) Borrar una contraseña
        5) Escribe "Salir" para salir del programa
        """)
    menu = input('Selecciona el numero de la operacion que vayas a realizar: ')

    

    # Introducir nuevas contraseñas
    if menu == "1":

        idenfiticador = input('Introduce la URL:  ')
        valor = input('Introduce la contraseña:  ')

        if idenfiticador not in database:
            database.insert({"url":idenfiticador, "password":valor})
            
        else:
            print('Esa contraseña ya existe')    
        print(database)
    # Mostrar contraseñas
    elif menu == "2":
        print(database.all())
        idenfiticador = input('¿Que contraseña quieres mostrar? ')

       
            
        result = database.search(selector.url == str(idenfiticador))

        if len(result) < 0:
            print('Esa contraseña no existe')
        else:
            result = database.search(selector.url == str(idenfiticador))
            print(f"la contraseña es {result[0]['password']}")
             
            salir = True
    # Actualizar contraseña
    elif menu == "3":

        print(database.search(selector.password == 'password'))
        password = input('Cual es la contraseña que quieres actualizar: ')
        update = input('Escribe la nueva contraseña: ')
        database.update({'password':update}, selector.url == str(password))

    elif menu == "4":
        print(database.all())
        delete = input('Que contraseña quieres borrar?')
        database.remove(selector.url == str(delete))

    elif menu in ["Salir","salir"]:
        salir = True
            
print('Fin')  


    