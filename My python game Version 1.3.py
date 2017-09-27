import random
import time

print("Welcome to my fighting game!")
print("The attacks are:")
print(" Punch | 50% chance \n Super Punch | 20% chance \n Heavy | 30% chance")

enemyhealth = 100
yourhealth = 100

while enemyhealth > 0:
    attack = input("What is your attack? ")

###Punch Hit Senction###
    if attack == "Punch":
        h = random.randint(1,10)
        random.randint(1,10)
        if h >= 5 :
            enemyhealth = enemyhealth - h
            print("HIT!","Damage:", h, "Enemy Health Remaining:" , enemyhealth)
            h = random.randint(1,10)
        else:
            print("MISS! Enemy Health Remaining:" , enemyhealth)
            h = random.randint(1,10)
            print("Enemys Turn!")
            et = ["Heavy", "Punch", "Super Punch"]
            
            
###Punch Hit Senction###

###Heavy Hit Section###
    if attack == "Heavy":
        h = random.randint(1,35)
        random.randint(1,35)
        if h >= 20 :
            enemyhealth = enemyhealth - h
            print("HIT!","Damage:", h,"Enemy Health:", enemyhealth)
            h = random.randint(1,35)
        else:
            print("MISS!", h, "Enemy Health Remaining:" , enemyhealth)
            h = random.randint(1,10)
###Heavy Hit Section###

###Super Punch###
    if attack == "Super Punch":
        h = random.randint(1,50)
        random.randint(1,50)
        if h >= 40 :
            enemyhealth = enemyhealth - h
            print("HIT!","Damage:", h, "Enemy Health Remaining:" , enemyhealth)
            h = random.randint(1,50)
        else:
            print("MISS! Enemy Health Remaining:", enemyhealth)
            h = random.randint(1,50)
            print("Enemys Turn!")
###Super Punch###

else:
    print("You Won")
    












  
