import os
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    name = os.environ['NAME']
    age = os.environ['AGE']

    return {'Olá': f'Eu sou o {name} e tenho {age} anos.'}