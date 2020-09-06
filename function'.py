#  how to create function

def testing():
    "first line"
    print("define function :: ")
    "ddddd"
    return print("return value")
    print("aftre return line will not print")

testing()

print("___________________________________________________________________")
# first type of function
def parameterlessfunction():
    print("parameter less function, which is not take any argument and not returning value")

parameterlessfunction()

print("___________________________________________________________________")

# Second type of function >> with parameter
def sum(a,b):
    c=a+b
    print("print of 2 number " + str(c))

sum(10,20)

print("___________________________________________________________________")

# Third type of function  taking parmeters and return the value

def multi(a,b):
    c=a*b
    print("multiplication of two number :: "+ str(c))
    return c

mu=multi(4,20)

sum(mu,10)

print("___________________________________________________________________")

# fourth type of function  taking no parmeters and return the value

def retdata():
    a=10
    return a

x= retdata()
print(x)



