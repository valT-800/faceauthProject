
from datetime import date, datetime

def detect_late_workers(worker):
    arriving_time_str = datetime.now().time().strftime("%H:%M:%S")
    arriving_time = datetime.strptime(arriving_time_str, "%H:%M:%S")

    begins_at = datetime.strptime(worker.begins_at, "%H:%M:%S")

    late_time_sec = (arriving_time - begins_at).seconds
    late_time_str = datetime.fromtimestamp(late_time_sec).strftime("%H:%M:%S")
    late_time = datetime.strptime(late_time_str, "%H:%M:%S").time()

    max_late = datetime.strptime("00:05:00", "%H:%M:%S").time()

    print("Max late ", max_late)
    if(late_time>max_late):
        with open(f'{date.today()}_late_workers.txt', 'a') as file:
            file.write(f'Id: {worker.id}, Name: {worker.first_name} ' f' {worker.last_name}, Late for: {late_time}\n')
        f = open(f'{date.today()}_late_workers.txt', "r")
        print(f.read())

