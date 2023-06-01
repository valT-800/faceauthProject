import pyodbc as pyodbc

class DatabaseConnection:
    def __init__(self):
        cnxn_str = ("Driver={SQL Server};"
                    "Server=.\SQLEXPRESS;"
                    "Database=FaceAuth;"
                    "Trusted_Connection=yes;")
        self.connection = pyodbc.connect(cnxn_str)