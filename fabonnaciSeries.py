#  Take input from User and generate fabonnaci series

x = int(input("Please enter your number :  - "))

#  Define initial 2 values
a = 0
b = 1
print(a)
print(b)
while ((a + b) < x):
    b = a + b
    a = b - a
    print(b)

print ("2 way from for loop ")
c = 0
d = 1
for i in range(1, 14):
    if (14 > (c + d)):
        d = c + d
        c = d - c
        print(d)