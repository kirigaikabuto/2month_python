from person import Person
p1 = Person(3)
p1.set_info()
print(p1.username)
print(p1.password)

#если пользователя нет в базе но при этом вызывается set_info то тогда неоходимо вывести нет такого пользователя
