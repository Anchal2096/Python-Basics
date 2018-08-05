from random import randint

# create a list of play options
t = ["Stone", "Paper", "Scissors"]

# assign a random play to the computer
computer = t[randint(0, 2)]

# set player to False
player = False

while not player:
    # set player to True
    player = input("Stone, Paper, Scissors?")
    if player == computer:
        print("Computer = ", computer, "\nTie!")
    elif player == "Stone":
        if computer == "Paper":
            print("Computer = ", computer, "\nYou lose!", computer, "covers", player)
        else:
            print("Computer = ", computer, "\nYou win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer = ", computer, "\nYou lose!", computer, "cut", player)
        else:
            print("Computer = ", computer, "\nYou win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Stone":
            print("Computer = ", computer, "\nYou lose...", computer, "smashes", player)
        else:
            print("Computer = ", computer, "\nYou win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]
