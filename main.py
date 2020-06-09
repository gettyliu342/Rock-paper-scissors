import random


print("Rock paper scissors game. In this game, use number inputs to select your choice. \n Rock = 1, Paper = 2, Scissors = 3")
print("If there is an invalid input, selection will default to Rock")


print()
def Rounds():
    rounds = input("Number of rounds: ")
    return rounds

def choice():
    choice = {"1":"Rock", "2":"Paper", "3":"Scissors"}
    return choice

def outcome(outcome, move1, move2):
    if outcome == "Tie":
        message = "Tie Game!"
    elif outcome == "Win":
        message = (move1 + "beats" + move2 + " You Win!")
    else:
        message = (move2 + "beats" + move1 + " You Lose!")

rounds = Rounds()
choice = choice()

move1 = ""
move2 = ""

move1 = input("Rock, paper, scissors, shoot!: ")
try:
    move1 = choice[move1]
except:
    move1 = "Rock"

move2 = choice[str(random.randint(1,3))]

if move1 == "Rock":
    if move2 == "Rock":
        outcome = "Tie"
    if move2 == "Paper":
        outcome = "Lose"
    else:
        outcome = "Win"
elif move1 == "Paper":
    if move2 == "Paper":
        outcome = "Tie"
    if move2 == "Rock"
        outcome = "Win"
    else:
        outcome = "Lose"
else:
    if move2 == "Paper":
        outcome = "Win"
    if move2 == "Rock":
        outcome = "Lose"
    else:
        outcome = "Tie"

