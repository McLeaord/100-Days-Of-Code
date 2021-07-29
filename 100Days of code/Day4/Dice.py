import random
minimum = 1
maximum = 6
roll_more = "y"


while roll_more == "y":
    
    print("Rolling Dice")
    print("Player(A) : ", random.randint(minimum,maximum))
    print("Player(B) :", random.randint(minimum,maximum))
    roll_more = input("Roll Again?")
