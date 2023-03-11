from fastapi import FastAPI

app = FastAPI(title='Projecto para resenar peliculas', description='En este proyecto seremos capaces de resenar peliculas', version='1')



@app.get('/')
async def index():
    return 'Hola mundo, desde un servidor en FastAPI'


@app.on_event('startup')
def startup():
    print('El servidor va acomenzar')


@app.on_event('shutdown')
def shutdown():
    print('El servidor se encuentra finalizando')
    


@app.get('/about')
async def about():
    return 'about'
