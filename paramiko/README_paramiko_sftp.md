# Métodos SFTP

Aquí un par de métodos los cuales podemos utilizar con nuestros objetos SFTP de Paramiko. No dudo que no serán de mucha útilidad.

| Método                                                  | Acción                                             |
| :------------------------------------------------------ | :------------------------------------------------- |
| get(remotepath, localpath, callback=None)               | Descarga un archivo remoto al directorio local     |
| put(localpath, remotepath, callback=None, confirm=True) | Envía un archivo local al servidor remoto          |
| chdir(path)                                             | Cambia el directorio de trabjo actual              |
| chmod(path, mode)                                       | Modifica los permisos del archivo indicado         |
| mkdir(path, mode=511)                                   | Crea un nuevo directorio con permisos establecidos |
| rename(oldpath, newpath)                                | Renombra un archivo o folder                       |
| rmdir(path)                                             | Remueve un folder a partir de una dirección        |
| symlink(source, dest)                                   | Crea un enlace simbólico                           |

Si bien no son los únicos métodos, son los que considero yo, con los que más estaremos trabajando en nuestro día a día. En caso quieras echar un vistazo a la documentación oficial aquí te dejo [el link](http://docs.paramiko.org/en/stable/api/sftp.html).