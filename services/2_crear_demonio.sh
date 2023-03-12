# super editor dirctory name file.service
# crear en el directory
sudo vim /etc/systemd/system/codigofacilito.service

# file codigofacilito.service

# start services
sudo systemctl enable codifofacilito

sudo systemctl start codigofacilito

sudo systemctl status codigofacilito.services

sudo systemctl stop codigofacilito.services

# reload deamon services
sudo systemctl reload codigofacilito

#
sudo systemctl deamon-reload

# el demonio se ejecuta en segundo plano
