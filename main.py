from fastapi import FastAPI
from tinydb import TinyDB, Query
import uuid

app = FastAPI()

user_accounts = TinyDB('user_accounts.json')
selector = Query()

# Authentication endpoints
@app.post("/auth/register")
def auth_register(email, password,):
    

    if not email or not password:
        return{"msg":"No has enviado los datos correctos"}
    found = user_accounts.search(selector.email == str(email))
    if not found:
        account = []
        
        user_id = str(uuid.uuid4())
        user_accounts.insert({"user_id":user_id[:5],"email":email, "password":password, "accounts": account})
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
    user = user_accounts.search(selector.token == str(token))
    account_id_random = str(uuid.uuid4())
    if user:
        user[0]["accounts"].append({
            "account_id": account_id_random,
            "url": url,
            "username": username,
            "password": password
        })
        return user_accounts.update({"accounts": user[0]["accounts"]}, selector.token == str(token))
    else: 
        return {"msg":"Error"}
                        
    

@app.get("/users/{user_id}/accounts/{account_id}")
def get_account(user_id, account_id, token):
    result = user_accounts.search(selector.token == str(token))
    ok = result[0]["accounts"][0]["password"]
    if result:
        return {"msg": f"la contraseña es {ok}"}
    else:
        return{"msg":"No hay contraseña"}

    

@app.put("/users/{user_id}/accounts/{account_id}")
def update_account(user_id, account_id, token, url, username, password):
        user = user_accounts.search(selector.token == str(token))

        if user:
            account = user[0]["accounts"]
            for index, account in enumerate(account):

                if item['account_id'] == str(account_id):
                    
                    user[0]["accounts"][index]['url'] = str(url)
                    user[0]["accounts"][index]['username'] = str(username)
                    user[0]["accounts"][index]['password'] = str(password)
                    user_accounts.update({"accounts": user[0]["accounts"]}, selector.token == str(token))
        
                
                    return {"msg":"Usuario Actualizado!"}

            return {"msg": "Usuario no encontrado!!!!"}
                        
        else: 
            return {"msg":"Error"}
                   
        # Aqui te tienes que meter dentro de cada uno de los valores de la lista de accounts y te pones a buscar el que coincide con el account_id. Usa un bucle for. 
        # Después de encontrar el account y editarlo, actualizas la lista de accounts dentro de user y haces el update como está puesto abajo




@app.delete("/users/{user_id}/accounts/{account_id}")
def delete_account(user_id, account_id, token):
    user = user_accounts.search(selector.token == str(token))
    result = user_accounts.search(selector.token == str(token))
    
    if user:

        user_accounts.remove(selector.result[0]["accounts"][0]["account_id"] == str(account_id))
    
        return {'msg':'Contraseña eliminada'}
    else:
        return {"msg":"Error"}

    
    

