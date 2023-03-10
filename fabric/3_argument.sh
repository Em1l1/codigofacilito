# Crear folder
fab -H ip create_folder:folder=cody --user=eduardo

# listar archivos
fab -H ip show_dir --user=eduardo

# Eliminar folder 
fab -H ip delete_folder:folder=cody --user=eduardo
