winingNum=20
winingNumt=30
userInput=input("enter you number b/w 1-100: ")
userInput=int(userInput)

#and oparator
# if userInput>winingNum and winingNumt<userInput:
#     print("you win!!")
# else:
#     if userInput<winingNum:
#         print("too low number!!")
#     else:
#         print("too high")   

#or oparator
if userInput>winingNum or winingNumt<userInput:
    print("you win!!")
else:
    if userInput<winingNum:
        print("too low number!!")
    else:
        print("too high")   