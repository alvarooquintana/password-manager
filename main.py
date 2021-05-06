from fastapi import FastAPI
from tinydb import TinyDB, Query

app = FastAPI()

user_accounts = TinyDB('user_accounts.json')
selector = Query()

# Authentication endpoints
@app.post("/auth/register")
def auth_register(email, password):
    encontrado = user_accounts.search(selector.email == str(email))
    if not encontrado:
         user_accounts.insert({"email":email, "contrasena":password})
         return {"msg":"Usuario creado"}  
    else:
       return  {"msg":"Error ya existe"}

@app.post("/auth/login")
def auth_login(email, password):
    encontrado = user_accounts.search(selector.email == str(email))
    if not user_accounts:
        return{'msg':'el usuario no existe'}

    elif encontrado[0]['contrasena'] != password:
        return {'msg':'contraseña incorrecta'}

# Authenticated endpoints
@app.post("/users/{user_id}/accounts")
def create_account(user_id, token, url, username, password):
    if password not in user_accounts:
        user_accounts.insert({"url":url, "password":password})
        return {'msg':'Contraseña creada y url creada'}
                        
    else:
        return{'msg':'Esa contraseña ya existe'}

@app.get("/users/{user_id}/accounts/{account_id}")
def get_account(user_id, account_id, token):
    result = user_accounts.search(selector.url == str(user_id))

    if len(result) < 0:
        return{'msg':'Esa contraseña no existe'}
    else:
        result = user_accounts.search(selector.url == str(user_id))
        a = result[0]['password']
        print(f"la contraseña es *** {result[0]['password']} ***")
        return {'msg':f'la contraseña es {a}'}

@app.put("/users/{user_id}/accounts/{account_id}")
def update_account(user_id, account_id, token, url, username, password):
    user_accounts.update({'password':password}, selector.url == str(url))
    return {'msg': 'Contraseña actualizada'}

@app.delete("/users/{user_id}/accounts/{account_id}")
def delete_account(user_id, account_id, token):
    user_accounts.remove(selector.url == str(user_id))
    return {'msg':'Contraseña eliminada'}

    
    

