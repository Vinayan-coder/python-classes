####decorators #####
#are functions that enhaces other function
#args $kwargs
#its a higher order fuctions (a function as its arguement)
# def saymyname(fun):
#     def wrapper():
#         print("say my name")
#         fun()
#         print("you are right")
#     return wrapper
# @saymyname
# def add():
#     print("add 2 numbers")

# @saymyname
# def hello():
#     print("my name is vinayan")

# add()
# hello()



#args##

# return args

# print(add(5,6,8,2))
# def  fullname(*args,**kwargs):
#     print(kwargs)
# fullname(fname="robert",mname="downie",lname="jr",) "Ironman"

# import time
# print(time.time())
# print(time.ctime())
# Start = time.time()
# for i in range(1,11):
#     print(i)
#     time.sleep(1)
# stop = time.time()
# print('total time:-',Start-stop)

import time
def totaltime(fun):
    def wrapper(*args,**kwargs):
start
for i in range():
    print(i)
    time.sleep(5)
stop = time.time()
print('total time:-',Start-stop)
