print("Welcome to the Treasure Island")
print("Your mission is to find the Treasure ")
choice1 = input("You're at a crossroad. where do you want to go? Type right or left").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake.There is an island in the middle of the lake. Type wait to wait for a "
                     "boat or Type swim to swim across.").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and "
                         "one blue. Which colour do you choose?").lower()
        if choice3 == "yellow":
            print("Great! You Win the game")
        elif choice3 == "red":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "blue":
            print("It's a room full of fire. Game Over.")
        else:
            print("You choose a door doesn't exist")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("ops! the fire burn you")
