userName=input("enter you name: ")
userAge=input("enter you age: ")
userAge=int(userAge)

if userAge>10 and (userName[0]=='a' or userName[0]=='A'):
    print("you can watch this movie!!")

elif userAge==11:
    print("user 11 year old")
    
else:
    print("you can not watch this movie!!")
   