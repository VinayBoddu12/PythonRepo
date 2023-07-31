import random

def userentries():
    global in3
    in3 = input("enter your choice: ")
    if (in3 != 's' and in3 != 'S' and in3 != 'w' and in3 != 'W' and in3 != 'g' and in3 != 'G'):
        raise ValueError("Please enter your letters as described above")

def computerentries():
    global comp
    comp = random.randint(0, 2)
    if (comp == 0):
        S = 'S'
        print("Computer Choice: ", S)
    elif (comp == 1):
        W = 'W'
        print("Computer Choice: ", W)
    else:
        G = 'G'
        print("Computer Choice: ", G)

def comparison():
    if (in3 == 's' or in3 == 'S'):
        s = 0
        if (s == 0 and comp == 0):
            print("It's a Draw")
        elif (s == 0 and comp == 1):
            print("You won")
        else:
            print("You lost")
    elif (in3 == 'w' or in3 == 'W'):
        w = 1
        if (w == 1 and comp == 0):
            print("You lost")
        elif (w == 1 and comp == 1):
            print("It's a Draw")
        else:
            print("You won")
    elif (in3 == 'g' or in3 == 'G'):
        g = 2
        if (g == 2 and comp == 0):
            print("You won")
        elif (g == 2 and comp == 1):
            print("You lost")
        else:
            print("It's a Draw")


def RulesOfGame():
    print("\t\t\t\tWelcome to the game,\nYou are playing **Tic Tac Toe** developed my Vinay Boddu")
    print("\n\nLet me explain you the rules of the game,\nthis is a one player game and you will be playing with the computer")
    print("\nRules::\n1. For snake, you need to enter 's' or 'S'")
    print("2. For Water, you need to enter 'w' or 'W'")
    print("3.For Gun, you need to enter 'g' or 'G'")
    print("\nSnake can swim in water, so snake wins.\nGun can kill Snake, Gun wins.\nBullets won't work in water, so water wins")
    print("\nif you chooses snake and computer chooses snake, then it's a draw")
    print("if you chooses snake and computer chooses water, then you won")
    print("if you chooses snake and computer chooses gun, then computer won and so on")

    print("\n\t\t\t\tI hope you got the game, let's continue")

def BasicInput():
    in1 = input("\nenter 'y' or 'Y' for continue:  ")
    if (in1 != 'y' and in1 != 'Y'):
        raise ValueError("Please enter 'y' or 'Y' to continue and do not enter any other words or letters or numbers")
    print("\nNow, you can enter your value ex: 's' or 'S' for Snake, 'w' or 'W' for Water and 'g' or 'G' for Gun\n")
    in2 = int(input("let me know, how many times you want to play: "))
    if (in2 > 0 or in2 < 100):
        for i in range(0, in2):
            userentries()
            computerentries()
            comparison()
    else:
        raise ValueError("enter number below 100")