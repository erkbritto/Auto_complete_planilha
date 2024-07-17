token:str = ''

def get_token():
    return token

def update_token():
    global token
    token = input('Insira o token: ')