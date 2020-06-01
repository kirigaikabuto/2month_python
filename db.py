import psycopg2

class Database:
    def __init__(self,db_name):
        self.connect = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="passanya",
            dbname=db_name
        )
    #select
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
    #insert,update,delete
    def save(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()



