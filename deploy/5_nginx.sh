# instalar el servidor nginx
sudo apt install nginx

# Crear la configuarcion de nginx
sudo nvim /etc/nginx/sites-available/python-web

# crear link
sudo ln -s /etc/nginx/sites-available/python-web /etc/nginx/sites-available

# verificar que la configuarcion fue un exito
sudo nginx -t

cat /etc/nginx/sites-available/python-web

# reiniciar el servidor nginx
sudo systemctl restart nginx
