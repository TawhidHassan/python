winningNm=43
guess=1
number=int(input("gusess a number berween 1 nad 100: "))
game_over=False

while not game_over:
    if number==winningNm:
        print(f"you wine :and you guesses this number in {guess} time")
        game_over=True
    else:    
        if number<winningNm:
          print("your guess low")
          guess+=1
          number=int(input("gusess a number again:  "))
        else:    
           print("your guess high")
           guess+=1
           number=int(input("gusess a number again:  "))


