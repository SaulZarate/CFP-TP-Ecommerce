
import mysql.connector
from .config import *

class Conection:

    def __init__(self):
        self.__conection = mysql.connector.connect(
            host = DATABASE_HOST ,
            user = DATABASE_USER,
            password = DATABASE_PASSWORD,
            database = DATABASE_NAME
        )
        
    def get_conection(self):
        return self.__conection
