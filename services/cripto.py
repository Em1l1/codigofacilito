import logging
import requests


# DEBUG
# INFO
# wARNING
# ERROR
# CRITICAL

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(threadName)s -  %(processName)s -%(levelname)s - %(message)s',
                    filename='codigofacilito.log',
                    filemode='a')

def get_current_price(id):
    logging.debug('Entramos a la funcion get_current_price.')

    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd')

    if response.status_code == 200:
        logging.info('La respuesta fue exitosa.')

        return response.json()
    else:
        logging.warning('No fue possible obtener una respuesta')

    return None


if __name__ == "__main__":
    response = get_current_price('bitcoin')
    logging.debug('Obtenemos una respuesta.')

    logging.info(response)
