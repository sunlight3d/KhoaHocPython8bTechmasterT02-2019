import math
from person import Person
x= 10
y = 12
print("x = "+str(x)+"y = "+str(y))
# print ("x = {}, y = {}".format(x, y))
z = x * y;
print("z = {}".format(z))

print("squared x = {}".format(x**10))
Person.base_salary = 123
person1 = Person("hoang", "hoang123@gmail.com", 20)
person2 = Person("Daniel", "daniel@gmail.com", 30)
person1.login()
person1.login()
person1.login()
person2.base_salary = 333
print(str(person1))

print(str(person2))