print("Welcome to your virtual pet!")
hunger = 0
tired = 0
happy = 5

pet_name = input("What would you like to name your pet? ")


print(f"{pet_name} is happy to meet you!")

while True:
    action = input("What do you want to do? (feed/play/sleep/quit) ")
    
    if action == "quit":
        print("Goodbye!")
        break
    elif action == "feed":
        food = input("What do you feed your pet?")
        if food == "cookie":
            print(f"You feed {pet_name} a cookie.")
            hunger = hunger - 2
        else:
            print(f"{pet_name} spits it out.")
    elif action == "sleep":
        print(f"You put {pet_name} to bed.")
    else:
        print(f"That action is invalid.")

    hunger = hunger + 1
    tired = tired + 1
    happy = happy - 1
