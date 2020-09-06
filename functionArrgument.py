'''
Different type of argument
-----------------------------
Required Argument
Keyword Argument
Default Argument
'''

# Required Argument if while calling function we have pass 2 argument sum(10,20) if we pass sum(10,) or sum(10)
# it will show "sum() missing 1 required positional argument: 'b'" in console
def sum(a,b):
    c=a+b
    print("print of 2 number " + str(c))

sum(10,2)

# Keyword Arrgument

def sumkeywordArgument(a,b):
    c=a+b
    print("print of 2 number " + str(c))

sum(b=10,a=2)


#Default Argument

def defaultArgumentsum(a,b=10):
    c=a+b
    print("print of 2 number " + str(c))

sum(50,200)  # alredy we have define b parameter as 10, if we pass the value while calling the function will consider

# alredy we have define b parameter as 10, if we pass dont pas value while
# calling the function will consider function default value as 10
sum(50)































