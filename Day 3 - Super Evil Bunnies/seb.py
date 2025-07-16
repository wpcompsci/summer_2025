import os
import time

INVENTORY = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_input(location):
    valid_inputs = {
        "old_oak": ["p", "e", "r"],
        "rainbow_falls": ["o", "p"],
        "pixie_housing": ["o", "r", "e"],
        "evil_bunnies": ["o", "p"],
    }
    while True:
        destination = input("Where do you want to go? ")
        if destination in valid_inputs[location]:
            return destination
        else:
            print("You can't go there from here. Please try again.")


def old_oak():
    clear_screen()
    while True:
        print("\nYou have found the OLD OAK. \n"
              "If it is wisdom you seek, well, you might have some luck. \n"
              "If you just want acorns, there's a bunch of those too. \n"
              "It is the wisest oak tree in the whole forest. \n"
              "What would you like to do? \n"
              "(t) Take an acorn \n"
              "(l) Leave the OLD OAK \n")
        action = input(">>>")
        if action == 't':
            if "acorn" in INVENTORY:
                print("You already have an acorn.")
            else:
                INVENTORY.append("acorn")
                print("You have taken an acorn.")
        elif action == 'l':
            print("\nAvailable destinations: \n"
                  "(p) Pixie Housing \n"
                  "(e) Evil Bunnies\n"
                  "(r) Rainbow Falls")

            destination = validate_input("old_oak")
            if destination == 'p':
                pixie_housing()
            elif destination == 'e':
                evil_bunnies()
            else:
                rainbow_falls()
        else:
            print("Invalid input. Please try again.")
            time.sleep(1)
            clear_screen()


def rainbow_falls():
    clear_screen()
    while True:
        print("\nYou have found the RAINBOW FALLS. \n"
              "The rainbows are very colorful and love to dance. \n"
              "They will dance for you if you ask nicely. \n"
              "What would you like to do? \n"
              "(a) Ask the rainbows to dance \n"
              "(l) Leave the RAINBOW FALLS \n")
        action = input(">>>")
        if action == 'a':
            print("The rainbows dance for you. You feel happy.")
        elif action == 'l':
            print("\nAvailable destinations: \n"
                  "(o) Old Oak\n"
                  "(p) Pixie Housing")

            destination = validate_input("rainbow_falls")
            if destination == 'o':
                old_oak()
            else:
                pixie_housing()
        else:
            print("Invalid input. Please try again.")
            time.sleep(1)
            clear_screen()


def pixie_housing():
    clear_screen()
    while True:
        print("\nYou have found the PIXIE HOUSING. \n"
              "The pixies are very friendly and love to dance. \n"
              "They will tell you a secret if you ask nicely. \n"
              "What would you like to do? \n"
              "(s) Ask the pixies for a secret \n"
              "(l) Leave the PIXIE HOUSING \n")
        action = input(">>>")

        if action == 's':
            print("The pixies tell you a secret, 'Bunnies hate acorns.'")
        elif action == 'l':
            print("\nAvailable destinations: \n"
                  "(o) Old Oak \n"
                  "(r) Rainbow Falls\n"
                  "(e) Evil Bunnies")
            destination = validate_input("pixie_housing")
            if destination == 'o':
                old_oak()
            elif destination == 'r':
                rainbow_falls()
            else:
                evil_bunnies()
        else:
            print("Invalid input. Please try again.")
            time.sleep(1)
            clear_screen()


def evil_bunnies():
    clear_screen()
    print("\nYou have found the EVIL BUNNIES. \n"
          "They are very evil and love to bite. \n"
          "They will fight you if you don't run away. \n"
          "What would you like to do? \n"
          "(f) Fight the EVIL BUNNIES \n"
          "(r) Run away \n")
    action = input(">>>")
    if action == 'f':
        if "acorn" in INVENTORY:
            print(
                "You throw the acorn at the bunnies.\n "
                "They run away, never to be seen again.\n "
                "You have saved the Super Happy Magic Forest. \n"
                "Congratulations!")
            end()
        else:
            print("The bunnies bite you. You lose.")
            end()
    elif action == 'r':
        print("\nWhere do you run: \n"
              "(o) Old Oak\n"
              "(p) Pixie Housing")
        destination = validate_input("evil_bunnies")
        if destination == 'o':
            old_oak()
        else:
            pixie_housing()
    else:
        print("You were too slow. The bunnies bite you. You lose.")
        end()
        time.sleep(1)


def end():
    time.sleep(5)
    clear_screen()
    print("You are at the end of the game.")
    print("Thank you for playing.")
    input("Press Enter to exit.")
    quit()


clear_screen()
print("Welcome to the SUPER HAPPY MAGIC FOREST!!!\n"
      "Here everybody enjoys picnics, fun, and dancing all year round.\n"
      "Enjoy the rainbows, sunshine and good times.\n"
      "Well the used to, but some things are not right.\n")
input("Press Enter to start the game.")

old_oak()
