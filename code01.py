import constant
print("code running")
a = 10
b = a**2
dval = 22
dVal = 15
c = a + dVal
print("the result: ",dval,a," is:",c)

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)

def add(a,b):
    """this function adds two numbers"""
    print(a+b)
    add(11,23)
    print(add._doc_)

for i in range(1,11): 
   print(i) 
   if i == 5:
       break

print(type(a))

c,a,b=5,3.2,"Hello"
print(a)
print(b)
print(c)

def to_naira(x):
    y=constant.DOLLAR
    z=x*y
    print(x,"naira is:",z,"naira")
to_naira(500)

in_x=input("enter an amount to convert")
in_put=int(in_x)
print("value entered is", in_x)
to_naira(in_put)

print("Use the following products codes")
print("mlk-->MILK , brd-->BREAD")
item=input("Enter item you wish to buy ")
qty=input("Enter the quantity ")

if item=="mlk":
    price=500
    total = int(qty)*price
    print("Total is :", total)
if item=="brd":
    price=400
    total= int(qty)*price
    print("Total is :", total)