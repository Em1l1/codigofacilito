# install dependency
sudo apt-get install python3-pip python3-dev python3-setuptools

sudo apt-get install build-essential libssl-dev libffi-dev

# creare el entorno virtual
python3 -m venv venv

# activar entorno virtual
source venv/bin/activate

# Ejecutar el proyesto
python manage.py runserver

 # agregar a config.py 
class ProductionConfig(DevelopmentConfig):
  DEBUG = False


config = {
  ....
  'production': ProductionConfig
}

# File manage.py
# cambiar por 
development => production


# levantar el servidor en production
# Agregando Banderas
python manage.py runserver -h "0.0.0.0" - p 5000
