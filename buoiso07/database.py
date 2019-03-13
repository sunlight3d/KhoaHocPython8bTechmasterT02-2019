import psycopg2
class Database:
    databaseObject = None;
    @staticmethod
    def get_instance():
        if(Database.databaseObject is None):
            Database.databaseObject = Database()
        return Database.databaseObject

    def __init__(self):
        try:
            self.connection_string = "dbname='pythontutorials' \
            user='postgres' host='localhost' password='123456'"
            self.connection = psycopg2.connect(self.connection_string)
            self.cursor = self.connection.cursor()
            print("Connect DB successfully")
        except Exception as ex:
            self.connection = None
            self.cursor = None
            print("Connect DB failed. Error: {}".format(ex))
        finally:
            pass
    def insert_new_product(self, product_name, year):
        try:
            sql = """INSERT INTO Products(productName, year) 
                VALUES(%s, %s)"""
            self.cursor.execute(sql, (product_name, year))
            self.connection.commit()
            return ("ok", "Insert data to Product successfully")
        except Exception as ex:
            return ("failed", "Insert data to Product failed.Error:{}".format(ex))
        