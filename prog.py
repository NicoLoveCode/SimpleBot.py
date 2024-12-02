# imports
import random as ran
import time 

# start? 
start = input("Would you like to start?\n")

if start.lower() == "yes":
    time.sleep(0.5)
    print("\nAlright, let's start the game...")
elif start.lower() == "no":
    time.sleep(0.5)
    print("\nIf you don't want to play, just don't click play 🙄🤦‍♂️")
    quit()

# where will you start your adventure?
camp_options = ["Beach", "Forest", "Rainforest", "Tundra", "Desert"]
camp = ran.choice(camp_options)
time.sleep(0.3)
print("You will be starting in the " + camp + "!")

# starting out
time.sleep(0.3)
start_message = "Welcome to the " + camp
print(start_message)
time.sleep(0.2)

# Possible inventory items
pos_beach_inv1 = ["Shells", "Rocks", "Sticks", "Fish"]
pos_beach_inv2 = ["Fish", "Turtle Shell", "Clams", "Bow", "Arrows"]
inv = ran.choice(pos_beach_inv1 + pos_beach_inv2)

time.sleep(1)
print("You looked around for a while and gathered some materials.")
time.sleep(0.2)
print("...")
time.sleep(0.5)

# Check inventory
if inv in pos_beach_inv1:
    print("You found some normal things, and also a washed-up fish. This is your current inventory: " + inv)
elif inv in pos_beach_inv2:
    print("You got lucky and found an old box with a bow and arrow! You used the arrows to get fish and collected some more food and items. This is your current inventory: " + inv)
else:
    print("This part has not yet been finished developing")