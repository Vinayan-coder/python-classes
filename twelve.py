# create a list of even and odd numbers from first 100 numbers
num = []
even = []
odd = []

for i in range(1,101):
    print(i)
    num.append(i)

for n in num:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even numbers:", even)
print("Odd numbers:", odd)




# create duplicate froim the list

c = [1,2,3,4,5,6,7,1,3,5,7]
b = []
for i in c:
    if i not in b:
        b.append(i)
print(b)



# break continue pass

#pass

age = 18
if age >=10:
    pass
b=10
print(b)

# continue


for i in range (1,11):
    if i ==6:
        continue
    print(i)


    #break
for i in range (1,11):
    if i ==6:
        break
    print(i)



#prime ir not

num = int(input('enter your num:---'))
prime = True
if num == 1:
    prime = False
else:
    for i in range(2,6):
        if num % i == 0:
            prime = False
            break
        







