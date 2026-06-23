# set 
# collection of data
# its unordered, unindexed and not contains duplicate values.

# fruits = {"mango","apple","banana","grape"}
# for i in fruits:
#     print(i)


# a={1,2,3,4,5,6}
# b={6,5,4,3,2,1}
# print(a==b)

# #list 
# a=[1,2,3,4]
# b=[4,3,2,1]
# print(a==b)



# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# print(a.union(b))
# print(a|b)
# print(a&b)
# print(a-b)
# print(b-a)
# print(a.intersection(b))


#dictionary
# is a key value paired datatypes

# userdata = {"name":"vinayan","age":35,"location":"kochi"}
# print(userdata)
# print(userdata["age"])

# data = {}
# data["name"] = 'vinayan'
# data["age"] = 35
# data["email"] = 'vinayan@gmail.com'
# data["phone"] = 985674432
# data["email"] = 'mohan@gmail.com'
# print(data)


#restriction of dictionary
#key are unique, keys are immutable, 
#we cannot provide key as list dictionary
#inbuild dictionary

a = {"name":"vinayan","age":35,"location":"kochi"}
print(a.get("name"))
print(a['location'])
print(a.keys())
print(a.values())
print(a.items())
a.update({'phone':967534256})
# a["age"] = 50
# a.pop('name')
# a.popitem()
# a.clear()
print(a)

data = ('name':"priya", 'age':40,'email':"vinayan@gmail.com")
for i in data:
print(i,data[i])
print(i,j, data[i])










