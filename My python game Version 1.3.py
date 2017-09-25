import random

hh = random.randint(1,25)
        
print("Welcome to my fighting game!")

enemyhealth = 100
while enemyhealth > 0:
    attack = input("What is your attack? ")
###Heavy Hit Section###
    if attack == "heavy":
        random.randint(1,25)
        if hh > 15 :
            enemyhealth = enemyhealth - hh
            print("HIT","Damage:", hh,"Enemy Health:", enemyhealth)
            hh = random.randint(1,25)
        else:
            print("MISS", hh, "Enemy Health Remaining:" , enemyhealth)
            
###Heavy Hit Section###
else:
    print("You Won")













  
