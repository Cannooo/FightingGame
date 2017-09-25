import random

x = random.randint(1,25)
        
print("Welcome to my game!")

enemyhealth = 100
while enemyhealth > 0:
    attack = input("What is your attack? ")

    if attack == "heavy":
        random.randint(1,25)
        if x > 10 :
            enemyhealth = enemyhealth - x
            print("Heavy Hit","Damage:", x,"Enemy Health:", enemyhealth)
            x = random.randint(1,25)
        else:
            print("Miss", x)
            break

else:
    print("You Won")













  
