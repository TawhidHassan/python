name="sifat"
age=22
print("name: "+name+" age: "+str(age))

name, age=input("enter your name and age ").split()

# String formatting
print("hello {} and your age is{}".format(name,age))#python 3
print(f"hello {name} and your age is {int(age)+10}")#python 3.6