name = "Alice"
print(name)
print (type(name))

data = "mohan's resume"
print(data)
print (type(data))

# ESCAPE SEQUENCE
qt = '''Gandhi once said, "Be the change you want to see in the world.'''
print(qt)
qt = "Gandhi\b once\t said, \"Be the change \byou want to\n see in the world.\""
print(qt)

# row string

qt = r"Gandhi once said, \"Be the change you want to see in the world.\""
print(qt)

input 
a = input("Enter a number --")
b = input("Enter another number --")
print (a)
print (b)
print (a + b)
# convert string to int
a = int(input("Enter a number --"))
b = int(input("Enter another number --"))
print(a + b)

name =  "mohan"
age = 25
married_status = False
rating = 4.5
result = "My name is {name} and my age is {age} and married status is {married_status} and rating is {rating}".format(name=name, age=age, married_status=married_status, rating=rating)
print(result)

i = 1
while i > 10:
    i = i + 1
    print(i)
    print("loop ended")




i = 1
esum = 0
osum = 0
while i <= 100:
    if i % 2 == 0:
        esum = esum + i
    else:
        osum = osum + i
    i = i + 1
print ("sum of even numbers is ", esum)
print ("sum of odd numbers is ", osum)







