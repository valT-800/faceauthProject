import face_train

from database.DatabaseConnection import DatabaseConnection
from face import detect_faces

from model.Company import Company
from repository.DatabaseRepository import get_workers

company = Company("My company")
database = DatabaseConnection()

cursor = database.connection.cursor()
company.workers = get_workers(cursor)

detect_faces(company)

