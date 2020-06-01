from db import Database

db1 = Database("27052020_users")

sql1 = "select * from product"
sql2 = "insert into product values (8,'sdsd',3000)"
db1.save(sql2)
products = db1.select(sql1)
print(products)