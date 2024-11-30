# imports
import random as ran
import time 

# start? 
start = input("Would you like to start?\n")

if start == "yes" or start == "Yes":
    time.sleep(0.5)
    print("\nAlright, lets start the game...")
elif start == "no" or start == "No":
    time.sleep(0.5)
    print("\nif you don't wanna play just dont click play 🙄🤦‍♂️")
    quit(

    )

# where will you start your adventure?
camp_options = ["Beach", "Forest", "Rainforest", "Tundra", "Desert"]
camp = ran.choice(camp_options)
time.sleep(0.3)
print("You will be starting in the " + camp + "!")

# starting out