import time
import requests
import logging

from cysystemd import journal

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

journald_handler = journal.JournaldLogHandler()
journald_handler.setFormatter(
        logging.Formatter('%(levelname)s - %(asctime)s - El precio de la cripto es: %(message)s')
)
logger.addHandler(journald_handler)

def get_current_price(id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd'

    response = requests.get(url)

    if response.status_code == 200:
        payload = response.json()
        return payload[id]['usd']


if __name__ == "__main__":
    while True:
        price = get_current_price('bitcoin')
        message = str(price) + '\n'

        logger.info(message)
        

        with open('prices.txt', 'a') as file:
            file.write(message)

        time.sleep(5)
