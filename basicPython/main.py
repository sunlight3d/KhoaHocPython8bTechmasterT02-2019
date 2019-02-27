import json
import re

x = "123.45"
x = float(x)
print(x)
print(float("123.45")+float("222.3"))
strA = "Hoang"
print(strA.lower())
fruits = ["banana", "orange", "apple"]
for fruit in fruits:
    print(fruit)
if "apple" in fruits:
    print("Co tim thay")
else:
    print("Khong tim thay")
cars = [
   {'name': 'Ford', 'year': 2005},
   {'name': 'Mitsubishi', 'year': 2000},
   {'name': 'Lexus', 'year': 2018},
]
#cars.sort(key=lambda car:car['year'])
#cars.sort(reverse=True,key=lambda car:car['year'])
#cars.sort(reverse=True,key=lambda car:car['name'])
cars.append({'name': 'Toyota', 'year': 2014})
cars.insert(1, {"name": "Vinfast", "year": 2019})
for car in cars:
    print('My car is : {}'.format(car))
tuple_fruits = ('orange', 'kiwi', 'mango')
# tuple_fruits[1] = 'banana'
print(tuple_fruits)
flowers = {"rose", "violet", "sunflower"}
flowers.add("hoa lan")
for flower in flowers:
    print('flower = {}'.format(flower))
mrHoang = {"name": "Hoang", "age": 30}
# mrHoang["email"] = "hoang123@gmail.com"
print(mrHoang)
for (key, value) in mrHoang.items():
    print("key = {}, value = {}".format(key, value))
if ("email" in mrHoang):
    print("Da co truong email")
else:
    print("chua co truong email")
if(len(mrHoang) > 0):
    print('This object has properties')
else:
    print('This object has no properties')
"""Convert a text of JSON to Dictionary"""
json_text = '{"name": "Hoang", "email": "hoang@gmail.com"}'
json_person = json.loads(json_text)
print(json_person)
student = {"name": "Alex", "dob":"2000-12-12"}
text_student = json.dumps(student)
print(text_student)
if(re.match('^The.*Spain$', 'The rain is in Spain')):
    print("Tim thay roi")
else:
    print("ko tim thay")
listResult = re.findall('^The.*Spain$', 'The rain is in Spain')
for x in listResult:
    print(x)
points = [{"3.2", "2.3"},("5.7", "26.3"), ("5.8", "26.3")]

# for point in points:
#     if(point[0]=="5.8"):

dict_points = {"3.2": "2.3", "5.7":"26.3", "5.8": "26.3"}
dict_points["5.8"]