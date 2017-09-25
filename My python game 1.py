print("Welcome to my game!")

enemyhealth = 100
while enemyhealth > 0:
    attack = input("What is your attack? ")
    if attack == "heavy":
        enemyhealth = enemyhealth - 50
    if attack == "medium":
        enemyhealth = enemyhealth - 25
else:
    print("You Won")








  
