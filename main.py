from fastapi import FastAPI
from tinydb import TinyDB, Query
import uuid

app = FastAPI()

user_accounts = TinyDB('user_accounts.json')
selector = Query()

# Authentication endpoints
@app.post("/auth/register")
def auth_register(email, password):
    if not email or not password:
        return{"msg":"No has enviado los datos correctos"}
    found = user_accounts.search(selector.email == str(email))
    if not found:
        user_id = str(uuid.uuid4())
        user_accounts.insert({"user_id":user_id[:5],"email":email, "password":password})
        return {"msg":"New user"}  
    else:
       return  {"msg":"Error, the user already exists"}

@app.post("/auth/login")
def auth_login(email, password):
    if not email or not password:
        return {"msg":"No has enviado los datos correctos"}
    encontrado = user_accounts.search(selector.email == str(email))
    #email_and_password = user_accounts.search(selector.contrasena == str(password))
    if not encontrado:
        return{'msg':'el usuario no existe'}

    elif encontrado[0]['password'] != password:
        return {'msg':'contraseña incorrecta'}
    else:
        token = str(uuid.uuid4())
        user_accounts.update({"token":token}, selector.email == email)
        return token
        

# Authenticated endpoints
@app.post("/users/{user_id}/accounts")
def create_account(user_id, token, url, username, password):
    if user_id not in user_accounts:
        user_accounts.insert({"user_id":user_id,"url":url,"token":token,"username":username,"password":password})
        return {'msg':'Contraseña creada'}
                        
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

    
    

