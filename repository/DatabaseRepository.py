
from model.Worker import Worker


def get_workers(cursor):
    workers = []

    sql = ("SELECT * FROM Workers")
    cursor.execute(sql)
    record = cursor.fetchall()

    for row in record:
        split = row[6].split('.')
        begins_at = split[0]
        worker = Worker(row[0], row[1], row[2], row[3], row[4], row[5], begins_at)
        print(row)
        workers.append(worker)
    return workers