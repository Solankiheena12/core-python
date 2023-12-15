price=90
txt="pay order of dollars {}"
print(txt.format(price))

price=25
txt="price is {} dollars"
print(txt.format(price))


price=56
txt="price is only {:.2f} dollars"
print(txt.format(price))

price=45
txt="price is only {:.3f} dollars"
print(txt.format(price))


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

itemno=25
price=500
quantity=2
quality="good"
myorder="i want {} pieces of item number {} for {:.2f} dollars and its quality is {}."
print(myorder.format(quantity,itemno,price,quality))


price = 40
quantity = 7
itemno = 126
myorder="i want {0} peace of item number {1} for {2:.2f} dollar"
print(myorder.format(price,quantity,itemno))

price=20
quantity=1
itemno=125
myorder="i want {1} peace of item number {2} for {2:.3f} dollars"
print(myorder.format(price,quantity,itemno))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

age=10
name="bansi"
txt="his name is {1}. {1} is {0} years old."
print(txt.format(age, name))


myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

myorder="i have a {carname}, it is a {price} dollars costly."
print(myorder.format(carname="Thar", price=13000 ))

