from tinydb import TinyDB, Query

 


# Data base

database = TinyDB('db.json')
autenticacion = TinyDB('autenticacion.json')

selector = Query()

salir = False
esc = False

while not salir:
    # Registro/Inicio de sesion
    
    print(""" 
        # 1) Registrarte
        # 2) iniciar sesion
        """)     
    initial_action = input('Elige 1 o 2 para lo que vayas a realizar: ')

    if initial_action == "1":

        email = input('Teclea tu correo electronico: ')
        password = input('Teclea tu contraseña: ')
        encontrado = autenticacion.search(selector.email == str(email))
        if not encontrado:
            autenticacion.insert({"email":email, "contrasena":password})  
        else:
           print('Error, el usuario ya existe')


    # Verificar identidad
    elif initial_action == "2":
        for item in autenticacion:
            print(item)
        email = input('teclea tu correo electronico: ')
        password = input('teclea tu contraseña: ')

        encontrado = autenticacion.search(selector.email == str(email))
        if not encontrado:
            print('el usuario no existe')

        elif encontrado[0]['contrasena'] != password:
            print('contraseña incorrecta')

        else:
            
            while not esc:
                print("hola")
            
                print("""
                    # 1) Nueva Contraseña   
                    # 2) Mostrar Contraseña
                    # 3) Actualizar Contraseña
                    # 4) Borrar una contraseña
                    # 5) Escribe "Salir" para salir del programa
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
                    
                # Mostrar contraseñas
                elif menu == "2":
                    for item in database:
                        print(f" - {item['url']}")
                    idenfiticador = input('¿Que contraseña quieres mostrar? ')

                    result = database.search(selector.url == str(idenfiticador))

                    if len(result) < 0:
                        print('Esa contraseña no existe')
                    else:
                        result = database.search(selector.url == str(idenfiticador))
                        print(f"la contraseña es *** {result[0]['password']} ***")
                        
                        
                # Actualizar contraseña
                elif menu == "3":

                    for item in database:
                        print(f" - {item['url']}")
                    
                    password = input('Cual es la contraseña que quieres actualizar: ')
                    update = input('Escribe la nueva contraseña: ')
                    database.update({'password':update}, selector.url == str(password))
                

                elif menu == "4":
                    for item in database:
                        print(f" - {item['url']}")

                    delete = input('Que contraseña quieres borrar?')
                    database.remove(selector.url == str(delete))

                elif menu in ["Salir","salir"]:
                    salir = True
                    pafuera = True
                else:
                    print('Operacion desconocida')

                
        
print('Fin')  


    