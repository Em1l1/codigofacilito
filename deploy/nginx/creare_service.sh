sudo vim /etc/nginx/sites-available/apiflask

# create link simbolik
sudo ln -s /etc/nginx/sites-availabe/project /etc/nginx/sites-enabled/

# restart nginx
sudo systemctl restart nginx.service