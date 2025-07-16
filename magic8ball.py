import random
import time

# magic 8 ball game
print("Welcome to the Magic 8 Ball game!")
input("What is your question? Press Enter to receive an answer...")

time.sleep(2)  # Pause for 2 seconds to build suspense
print("Thinking", end="")
print(".", end="")
time.sleep(1)  # Pause for 1 second
print(".", end="")
time.sleep(1)  # Pause for another second
print(".")
random_number = random.randint(1, 5)

if random_number == 1:
    print("Yes, definitely!")
elif random_number == 2:
    print("Ask again later.")
elif random_number == 3:
    print("My sources say no.")
elif random_number == 4:
    print("Outlook not so good.")
elif random_number == 5:
    print("You may rely on it.")