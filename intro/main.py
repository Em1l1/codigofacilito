import pymysql
# import mariadb

HOST = '172.20.0.2'

if __name__ == '__main':
    try:
        # connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='pythondb')
        connection = pymysql.Connect(host=HOST,
                             port=3307,
                             user='root',
                             password='t32la',
                             database='pythondb')
        # connect = mariadb.connect(host='127.0.0.1', port=3306, user='roots', password='123', db='pythondb')
        print('Conexion realizada de forma exitosa!!!')

    except pymysql.err.OperationalError as err:
    # except mariadb.err.OperationalError as err:
        print('No fue posible realizar la conexion')
        print(err)
