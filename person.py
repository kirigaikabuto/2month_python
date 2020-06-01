from db import Database

class Person:

    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password
        self.db = Database("27052020_users")
        self.table_name="persons"
        self.create_table()

    def create_table(self):
        sql=f"""
        create table if not exists {self.table_name}(
            id int primary key,
            username varchar(255),
            password varchar(255)
        );"""
        self.db.save(sql)

    def save_person(self):
        sql=f"insert into {self.table_name} values ('{self.id}','{self.username}','{self.password}')"
        self.db.save(sql)

    def get_all_persons(self):
        sql = f"select * from {self.table_name}"
        persons = self.db.select(sql)
        return persons
