import random


print("Rock paper scissors game. In this game, use number inputs to select your choice. \n Rock = 1, Paper = 2, Scissors = 3")
print("If there is an invalid input, selection will default to Rock")


print()
def Rounds():
    try:
        rounds = int(input("Number of rounds: "))
    except:
        rounds = 3
    return rounds

def choice():
    choice = {"1":"Rock", "2":"Paper", "3":"Scissors"}
    return choice

def result(outcome, move1, move2):
    if outcome == "Win":
        message = (move1 + "beats" + move2 + " You Win!")
    else:
        message = (move2 + "beats" + move1 + " You Lose!")
    return message

def OUTCOME():
    if move1 == "Rock":
        if move2 == "Rock":
            outcome = "Tie"
            message = "Tie Game!"
            print(message)
        elif move2 == "Paper":
            outcome = "Lose"
            message = result(outcome, move1, move2)
            print(message)
        else:
            outcome = "Win"
            message = result(outcome, move1, move2)
            print(message)
    elif move1 == "Paper":
        if move2 == "Paper":
            outcome = "Tie"
            message = "Tie Game!"
            print(message)
        elif move2 == "Rock":
            outcome = "Win"
            message = result(outcome, move1, move2)
            print(message)
        else:
            outcome = "Lose"
            message = result(outcome, move1, move2)
            print(message)
    else:
        if move2 == "Paper":
            outcome = "Win"
            message = result(outcome, move1, move2)
            print(message)
        elif move2 == "Rock":
            outcome = "Lose"
            message = result(outcome, move1, move2)
            print(message)
        else:
            outcome = "Tie"
            message = "Tie Game!"
            print(message)

rounds = Rounds()
choice = choice()


move1 = ""
move2 = ""
outcome = ""
counter = 1

while int(rounds) > 0:
    print("Round", counter)
    move1 = input("Rock (1), paper (2), scissors(3), shoot!: ")
    try:
        move1 = choice[move1]
    except:
        move1 = "Rock"
    move2 = choice[str(random.randint(1,3))]
    counter += 1
    rounds -= 1


    OUTCOME()




