import random
# print(random.randint(1,10))

# fruits = ["apple","orange","pineapple","grapes","mango"]
# print(random.choice(fruits))

# coin = ["head","tail"]
# print(random.choice(coin))

# paper rock scissor

# data = ("rock","scissor","paper")

# player = input("data")
# comp = input("data")
# if player == "rock" or "scissor" or "paper":

# ch = ['rock', 'paper', 'scissor']
# comp = random.choice(ch)
# player = ""
# while player not in ch:
#     player = input("enter your choice rock/scissor/paper :-").lower()
# print(f"player :- {player} \ncomputer :- {comp}")
# if player =="rock":
#     print ("its a tiee !!!")
# elif comp =="rock":
#     if player =="scissor":
#         print("rock smashes scissor computer wins")
#     else:
#         print("paper covers rock player wins")
# elif comp =="paper":
#     if player =="rock":
#         print("paper covers rock computer wins")
#     else:
#         print("rock beats scissor player wins")
# elif comp == "scissor":
#     if player =="paper":
#         print("scissor cut the paper computer wins")
#     else:
#         print("rock beats scissor player wins")

#create an RPG game
#player vs enemy

#player hp = 100
#enemy hp = 100

# def player_turn(player_hp, enemy_hp):
#     print(f"\nYour HP: {player_hp} | Enemy HP: {enemy_hp}")
#     action = input("Choose your action (attack/heal): ").lower()
    
#     if action == "attack":
#         damage = random.randint(10, 20)
#         enemy_hp -= damage
#         print(f"You attacked the enemy for {damage} damage!")
#     elif action == "heal":
#         heal_amount = random.randint(5, 15)
#         player_hp += heal_amount
#         print(f"You healed yourself for {heal_amount} HP!")
#     else:
#         print("Invalid action! You lose your turn.")
    
#     return player_hp, enemy_hp

import random
player = input("enter your name:- ").lower()
enemy = random.choice(['dragon', 'goblin', 'troll'])
playerhp = 100
enemyhp = 100
turn = 1
while playerhp > 0 and enemyhp > 0:
    print(f'Turn{turn}')
    print(f'{enemy} attacks player')
    playerhp = playerhp - random.randint(8,20)
    print(f'player hp {playerhp}')
    print(f'{player} strikes back')
    enemyhp = enemyhp - random.randint(8,20)
    print(f'enemy hp {enemyhp}')
    turn = turn+1
    if playerhp <=0:
        print(f'{enemy} won')
        break
    elif enemyhp <=0:
        

