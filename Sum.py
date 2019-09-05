a = int(input("Enter first value"))
b = int(input("Enter second value"))
c = int(input("Enter third value"))

def sum():
    if(a == b == c):
       Val = a * a * a
       print(Val)
    else:
        Val = a + b + c
        print(Val)

sum()
