# function

def grater(a,b):
    if a>b:
        return a
    else:
        return b

num1=int(input("enter 1 no: "))
num2=int(input("enter 2 no: "))
biger=grater(num1,num2)

print(f"{biger} is greated")