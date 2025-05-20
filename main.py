import datetime
import os
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()

startedAt = datetime.datetime.now()

@app.get('/')
def index():
    name = os.environ['NAME']
    age = os.environ['AGE']

    return {'Olá': f'Eu sou o {name} e tenho {age} anos.'}

@app.get('/health')
def health_check():
    duration = datetime.datetime.now() - startedAt

    if duration.seconds < 10:
        return Response(status_code=500)
    else:
        return JSONResponse(status_code=200, content={'status': 'ok'})