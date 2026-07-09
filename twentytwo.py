
#object oriented programing
#object based program
#real life entity

#object have 2
#attributes - define as a object
#behaviours/ methods- functions inside a class
#object  is an instance of class

#class - blueprint
#to create objects

# class car:
#     def start():
#         print("car has started")
#     def stop():
#         print("car has stopped")
# c1 = car
# c2 = car
# c3 = car
# c2.start()
# c2.stop()


# class bike:
#     def start():
#         print("cannot start")
#     def stop():
#         print("its not my bike")
# wrong_key = bike
# try_to_break = bike
# wrong_key.start()
# wrong_key.stop()
    
#constructor 
#used to initialize an object

# class car:
#     def __init__(self,n,c):
#         self.name = n
#         self.color = c
#     def start(self):
#         print(f'{self.name},{self.color} has started')
#     def stop(self):
#         print(f"{self.name},{self.color} car stopped")
# c1 = car("swift", "black")
# c2 = car("city","red")
# c1.start()
# c2.stop()

# create a class student
# with 6 attributes name m1, m2, m3, m4, m5
# 3 methods
# sum of marks()
# average of marks()
# display()

# class student:
#     def __init__(self, name,m1, m2, m3, m4, m5):
#         self.name = name
#         self.marks1 = m1
#         self.marks2 = m2
#         self.marks3 = m3
#         self.marks4 = m4
#         self.marks5 = m5
#     def sum(self):
#         print(f"{self.marks1}+{self.marks2}+{self.marks3}+{self.marks4}+{self.marks5}")
#     def average(self):
#         print(f"{self.marks1}+{self.marks2}+{self.marks3}+{self.marks4}+{self.marks5}")/5
#     def display(self):
#         print(f'student mark list\nm1= \nm2= \nm3= \nm4= \nm5= ')
# s1 = student("vinayan",45,39,44,43,41)
# s1.sum()
# s1.average()
# s1.display()

class student:
    def __init__(self,name, m1, m2, m3, m4, m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
    def sum_of_marks(self):
        return self.m1+self.m2+self.m3+self.m4+self.m5
    def average_of_marks(self):
        return self.sum_of_marks()/5
    def display(self):
        print(f'student {self.name} has marks of \n{self.m1} \n{self.m2} \n{self.m3} \n{self.m4} \n{self.m5}')
    s1 = student        




