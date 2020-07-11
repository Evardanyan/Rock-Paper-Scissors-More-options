import random

score_dict = {}
score = 0
out = open('rating.txt', 'r+')

name = str(input("Enter your name: "))
print(f'Hello, {name}')


for line in out:
    (key, val) = line.split()
    score_dict[(key)] = val


if name not in score_dict:
    score_dict[name] = score
else:
    score=int(score_dict.get(name))

word = ["paper", "rock", "scissors"]
option = ["rock", "paper", "scissors"]



option_input = input().split(",")

option = ["rock", "paper", "scissors"]

option_default = ["rock", "paper", "scissors"]


if len(option_input) == 1:
    option = option_default
    print("Okay, let's start")
elif len(option_input) > 1:
    option = option_input
    print("Okay, let's start")

word = ["!rating", "!exit"]

if  len(option_input) == 1:
    while True:
        choice = random.choice(option)
        text = input()
        if text == "!exit":
            print("Bye!")
            break
        if text == "!rating":
            score_dict[name] = score
            print("Your rating:", score_dict[name])

        if text not in word and text not in option :
            print("Invalid input")
        elif text ==  "rock" and choice == "paper":
             print(f"Sorry, but computer chose {choice}")
        elif text ==  "paper" and choice == "scissors":
            print(f"Sorry, but computer chose {choice}")
        elif text ==  "scissors" and choice == "rock":
            print(f"Sorry, but computer chose {choice}")

        elif text == choice:
            print(f"There is a draw ({choice})")
            score = score + 50
        elif text != '!rating':
            print(f"Well done. Computer chose {choice} and failed")
            score = score + 100

    print(name, score, sep=" ", file=out, flush=True)

elif len(option_input) > 1:
    while True:
        choice = random.choice(option)
        text = input()
        if text == "!exit":
            print("Bye!")
            break

        if text not in word and text not in option:
            print("Invalid input")

        elif text == "!rating":
            score_dict[name] = score
            print("Your rating:", score_dict[name])

        elif text == choice:
            print(f"There is a draw ({choice})")
            score = score + 50

        elif text == "rock" and (choice == 'paper' or choice == 'air' or choice == 'water' or choice == 'dragon' \
            or choice == 'devil' or choice == 'lightning'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "fire" and (choice == 'air' or choice == 'water' or choice == 'gun' or choice == 'dragon' \
            or choice == 'devil' or choice == 'lightning'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "scissors" and (choice == 'rock' or choice == 'water' or choice == 'gun' or choice == 'dragon' \
            or choice == 'devil' or choice == 'lightning'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "snake" and (choice == 'rock' or choice == 'fire' or choice == 'gun' or choice == 'dragon' \
            or choice == 'devil' or choice == 'lightning'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "human" and (choice == 'rock' or choice == 'fire' or choice == 'scissors' or choice == 'gun' \
            or choice == 'devil' or choice == 'lightning'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "tree" and (choice == 'rock' or choice == 'fire' or choice == 'scissors' or choice == 'snake' \
             or choice == 'lightning'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "wolf" and (choice == 'rock' or choice == 'fire' or choice == 'scissors' or choice == 'dragon' \
            or choice == 'human' or choice == 'snake'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "sponge" and (choice == 'rock' or choice == 'fire' or choice == 'scissors' or choice == 'snake' \
            or choice == 'human' or choice == 'tree'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "paper" and (choice == 'fire' or choice == 'scissors' or choice == 'snake' or choice == 'human' \
            or choice == 'tree' or choice == 'wolf'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "air" and (choice == 'scissors' or choice == 'snake' or choice == 'human' or choice == 'tree' \
            or choice == 'wolf' or choice == 'sponge'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "water" and (choice == 'snake' or choice == 'human' or choice == 'tree' or choice == 'wolf' \
            or choice == 'sponge' or choice == 'paper'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "dragon" and (choice == 'human' or choice == 'tree' or choice == 'wolf' or choice == 'sponge' \
            or choice == 'paper' or choice == 'air'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "devil" and (choice == 'tree' or choice == 'wolf' or choice == 'sponge' or choice == 'paper' \
            or choice == 'air' or choice == 'water'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "lightning" and (choice == 'wolf' or choice == 'sponge' or choice == 'paper' or choice == 'air' \
            or choice == 'water' or choice == 'dragon'):
            print(f"Sorry, but computer chose {choice}")

        elif text == "gun" and (choice == 'sponge' or choice == 'paper' or choice == 'air' or choice == 'water' \
            or choice == 'dragon' or choice == 'devil'):
            print(f"Sorry, but computer chose {choice}")

        else:
            print(f"Well done. Computer chose {choice} and failed")
            score = score + 100
    print(name, score, sep=" ", file=out, flush=True)
    
out.close()
