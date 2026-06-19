# lista are mutable
# strings are immutable

a = "[11,12,13,14,15]"
a[0] = "mohan"
print(a)

b = "mohan"
b[0] = "h"
print(b)





#inbuilt methods
# add elements
# append = adds an element at the end of the list





a = [11,12,13,14,15]
a.append(16)
print(a)

a.append(17)
print(a)

extend = [18,19,20]
a.extend(['mohan'])
print(a)



insert = [21,22,23]
a.insert(0, 21)
print(a)



# to remoove elements
a.remove(21)
print(a)

#pop = removes an element at a given index and returns the removed elemen

a.pop(0)
print(a)





