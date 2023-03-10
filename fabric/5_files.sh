# listar coandos
fab -l

# ejecutar comando enviar archivos

fab -H ip upload_txt_file --user=eduardo

# descargar archivo
fab -H ip get_txt_file --user=eduardo

# con argumentos
fab -H ip get_txt_file:file=README.md --user=eduardo
