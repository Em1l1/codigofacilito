import time
from datetime import datetime

if __name__ == "__main__":
    while True:
        now = datetime.now()
        current_now = now.strftime('%Y-%m-%d %H:%M:%S')

        with open('/home/robot/codigofacilito/servidor/services/dates.txt', 'a') as file:
            file.write(current_now + '\n')


        time.sleep(5)
