import mysql.connector


class Database:
    """class used to perform all the CRUD operations on MySQL DB"""

    def __init__(self):
        self.__connection = mysql.connector.connect(
            host='localhost', port=3306, user='root', password='root1234', database='mydb'
        )
        self.__cursor = self.__connection.cursor()

    def __del__(self):
        self.__connection.close()
        self.__cursor.close()

    def select(self, statement):
        self.__cursor.execute(statement)
        return self.__cursor.fetchall()

    def execute(self, statement):
        self.__cursor.execute(statement)
        self.__connection.commit()

