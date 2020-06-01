from person import Person

p1 = Person(id=1)
print(p1.username)
print(p1.password)
p1.set_info()
print(p1.username)
print(p1.password)
#setInfo()->возвращать информацию об этом человеке из
# базы и положить значения в текуший объект(ссылку) моего класса