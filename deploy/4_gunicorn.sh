# install gunicorn
pip install gunicorn

nano wsgi.py

# levantar el servidor con gunicorn /
gunicorn --bind 0.0.0.0:5000 wsgi:app

# crear y Generar servicion
sudo nvim /etc/systemd/system/python-web.service

cat /etc/systemd/system/python-web.service

# activar servicio
sudo systemctl start python-web
sudo systemctl enable python-web
sudo systemctl status python-web
