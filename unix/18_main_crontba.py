from datetime import datetime

now = datetime.now()
current_date = now.strftime('%Y-%m-%d %H:%M:%S')

with open('dates.txt', 'a') as file:
    file.write(current_date + '\n')