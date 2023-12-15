#if..elif..else  statement

if True:
    print("hello python if")

if 2>1:
    print("2 is grater than 1")


if 1>2:
    print("1 is grater than 2")
else:
    print("1 is not grater than 2")


if 1>2:
    print("1 is grater than 2")
elif 2>1:
    print("1 is not grater than 2")
else:
    print("1 is equal to 2")


num=1
while num <=10:
    print(num)
    num += 1

x=0
while x < 10:
    print(x)
    x += 1




for i in range(1,11):
    print(i)

for x in range(25,30):
    print(x)

for x in range(2, 9):
    print(x)


my_integers=[1,4,2,7,5,9,8]
print(my_integers[0])
print(my_integers[4])
print(my_integers[6])

relatives_name=[
    "bansi",
    "kishu",
    "alpa",
    "sapna",
    "vaishali",
    "hetal",
    "ruchi"
]
print(relatives_name)
print(relatives_name[3])


bookself=[]
bookself.append("hello everyone..")
bookself.append("how are you")
print(bookself[0])
print(bookself[1])

mylist=["bansi","mahi"]
mylist.append("kishu")
mylist.append("piyu")
print(mylist[2])
print(mylist[0])


dictionary_example={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
}
print(dictionary_example)

dictionary_ex={
    "name":"heena",
    "nickname":"heenu",
    "nationality":"indian"
}
print("my name is %s" %(dictionary_ex["name"]))
print("but you can also call me %s" %(dictionary_ex["nickname"]))
print("and by the way i'm %s" %(dictionary_ex["nationality"]))

dict1={
    "name":"bansi",
    "nickname":"pihu",
    "nationality":"indian"
}
print("my name is %s" %(dict1["name"]))
print("but you can also call me %s" %(dict1["nickname"]))
print("and han by the way %s" %(dict1["nationality"]))

dictionary_ex={
    "name":"kishu",
    "nickname":"piyu"
}
print("hello my name is %s" %(dictionary_ex["name"]))
print("but you can also call me %s" %(dictionary_ex["nickname"]))

dict1={
    "name":"heena",
    "nickname":"heenu",
    "nationality":"india"
}
dict1["age"]=20
print(dict1)

color={
    "color1":"red",
    "color2":"green",
    "color3":"blue"
}
color["color4"]="white"
color["color5"]="black"
print(color)



dictionary = { "some_key": "some_value" }
for key in dictionary:
    print("%s --> %s" %(key, dictionary[key]))

dictionary={"name":"heena"}
for key in dictionary:
    print("%s--->%s" %(key, dictionary[key] ))

dict1={"city":"rajkot"}
for key in dict1:
    print("%s--->%s" %(key, dict1[key]))

dict2={"name":"savan"}
for key in dict2:
    print("%s---%s" %(key, dict2[key]))


dictionary={"name":"heena"}
for key, value in dictionary.items():
    print("%s-->%s" %(key, value))

dict1={"name":"heena"}
for key,value in dict1.items():
    print("%s--->%s" %(key,value))

dict2={"name":"darshan"}
for key,value in dict2.items():
    print("%s--->%s" %(key, value))



dictionary={
    "name":"darshan",
    "nickname":"darshu",
    "city":"rajkot",
    "age":12
}
for attribute,value in dictionary.items():
    print("my %s is %s" %(attribute,value))

dict1={
    "name":"alpa",
    "city":"rajkot",
    "state":"gujarat"
}
for key,value in dict1.items():
    print("my %s is %s" %(key,value))



#create class and object:
class vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels=number_of_wheels
        self.type_of_tank=type_of_tank
        self.seating_capacity=seating_capacity
        self.maximum_velocity=maximum_velocity

tesla_model_s=vehicle(4, 'electric', 5, 250)

print(tesla_model_s.number_of_wheels)
print(tesla_model_s.type_of_tank)
print(tesla_model_s.seating_capacity)
print(tesla_model_s.maximum_velocity)


#getter and setter:
class vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels=number_of_wheels
        self.type_of_tank=type_of_tank
        self.seating_capacity=seating_capacity
        self.maximum_velocity=maximum_velocity

    def number_of_wheels(self):
        return self.number_of_wheels

    def set_number_of_wheels(self, number):
        self.number_of_wheels=number

tesla_model_s=vehicle(4, 'electric', 5, 250)

print(tesla_model_s.number_of_wheels)
print(tesla_model_s.type_of_tank)
print(tesla_model_s.seating_capacity)
print(tesla_model_s.maximum_velocity)

tesla_model_s.number_of_wheels=2
print(tesla_model_s.number_of_wheels)



#make_noice()
class vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels=number_of_wheels
        self.type_of_tank=type_of_tank
        self.seating_capacity=seating_capacity
        self.maximum_velocity=maximum_velocity
    
    def make_noice(self):
        print('VEVNOKDNVKJN')

tesla_model_s=vehicle(4, 'electric', 5, 250)

tesla_model_s.make_noice()

