class Company:
    def __init__(self, name):
        self.name = name
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def delete_worker(self, worker):
        pass

    def update_worker(self, worker):
        for w in self.workers:
            if worker.id == w.id:
                w=worker

    def get_worker(self, name_and_id):
        for worker in self.workers:
            name_id = worker.first_name + worker.last_name + str(worker.id)
            if name_and_id == name_id:
                return worker