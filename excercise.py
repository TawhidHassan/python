winingNum=20
userInput=input("enter you number b/w 1-100: ")
userInput=int(userInput)

if userInput==winingNum:
    print("you win!!")
else:
    if userInput<winingNum:
        print("too low number!!")
    else:
        print("too high")   