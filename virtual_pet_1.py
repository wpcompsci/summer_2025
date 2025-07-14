print("Welcome to your virtual pet!")

pet_name = input("What would you like to name your pet? ")

print(f"{pet_name} is happy to meet you!")

food = input(f"What would you like to feed {pet_name}? ")

if food == "cookie":
    print(f"{pet_name} wags its tail happily!")
else:
    print(f"{pet_name} sniffs the {food} and shrugs.")
