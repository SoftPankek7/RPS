import random
import os

actions = ["r", "p", "s"]
fondness = [2,2,2]

player_health = 100
player_fondness = [1,1,1]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def generate_action():
    # Add a bit of random noise
    if random.choice([True,False]):
        _ = str(random.choices(actions, weights=[abs(fondness[0] - player_fondness[1]),abs(fondness[1] - player_fondness[2]),abs(fondness[2] - player_fondness[0])]))[2]
    else:
        _ = str(random.choice(actions))

    print(_)
    if _ == "r":
        fondness[0] += 1
        print("I pick Rock.")
    elif _ == "p":
        fondness[1] += 1
        print("I pick Paper.")
    elif _ == "s":
        fondness[2] += 1
        print("I pick Scissors.")
    return _

wins = 0
losses = 0

def win():
    print("You Win!")
    global wins
    wins += 1
def lose():
    print("You Lose!")
    global losses
    losses += 1

while player_health >= 0:
    try:
        clear()
        player_action = input("Choice:  ").lower()
        #player_action = str(random.choices(actions, weights=[player_fondness[0],player_fondness[1],player_fondness[2]]))[2]
        if player_action.lower() not in actions:
            print(player_action+" is not an option.")
        else:
            if player_action.lower() == "r":
                player_fondness[0] += 1
            elif player_action.lower() == "p":
                player_fondness[1] += 1
            elif player_action.lower() == "s":
                player_fondness[2] += 1
            ai = generate_action()

            # Lose Conditions

            if ai == "r" and player_action == "s":
                lose()
            elif ai == "p" and player_action == "r":
                lose()
            elif ai == "s" and player_action == "p":
                lose()
            
            # Win Conditions

            elif player_action == "r" and ai == "s":
                win()
            elif player_action == "p" and ai == "r":
                win()
            elif player_action == "s" and ai == "p":
                win()

            # Draw Conditions

            else:
                print("You Draw!")

            input("[ ENTER ]")
    except KeyboardInterrupt:
        clear()
        print("The End.\n-------\nHere are your stats:\nWins: "+str(wins)+"\nLosses: "+str(losses))
        exit(0)