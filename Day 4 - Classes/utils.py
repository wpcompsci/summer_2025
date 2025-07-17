import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def end_game():
    time.sleep(3)
    clear_screen()
    print("You are at the end of the game.")
    print("Thank you for playing.")
    input("Press Enter to exit.")
    quit()
