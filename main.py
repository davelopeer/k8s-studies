import os
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    name = os.environ['NAME']
    age = os.environ['AGE']

    print(f'Olá, eu sou o {name} e tenho {age} anos.')

    return {'Olá': 'Mundo'}