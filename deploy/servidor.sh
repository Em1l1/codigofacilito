# instalar en el servidor
sudo apt install python3-pip python3-dev python3-venv

# Active virtualenv
pip install wheel


sudo apt install libmysqlclient-dev

# ejecutar project
uvicorn main:app --reload

# Exponer servidor
uvicorn --host 0.0.0.0 main:app