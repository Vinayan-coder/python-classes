# Exception
# try:
#     a = 5
#     b = 0
#     print(a/b)
# except Exception as e:
#     print("you have an error", e)
# print("mohan")


# try:
#     a = int(input("enter a number:- "))
#     b = 0
#     print(a/b)
# except ZeroDivisionError as e:
#     print("you cannot divide with zero")
# except ValueError:
#     print("check values")
# except TypeError:
#     print("check type")
# finally:
#     print("this will always excute")

# class myerror(Exception):
#     pass
# name ="das"
# if name == "das":
#     raise myerror("name should not be das")

# a = 5
# del(a)
# print(a)

# file1 = open("data.txt1","r")
# print(file1.read())
# file1.close()

# file2 = open("myfile.txt")
# file2.write("today is rainy day !!!!")
# file2.close()

# file3 = open("myfile.txt","w")
# file3.write("\n its a alchaholic day")
# for i in range(1,10):
#     file3.write(f"\nvinayan {i}")
# file3.close()



import os
os.mkdir("image") # for creating folder 
os.remove("data.txt1")
os.rename("myfile.txt","demo.txt")
pat = "C:\\Users\\Student\\Desktop\\VINAYAN\\day11\\nk.txt"
if os.path.exists(pat):
    if os.path.isfile(pat):
        print("file exists")
    elif os.path.isdir(pat):
        print("folder exists")
           
