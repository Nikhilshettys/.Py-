import random

low = 1
high = 100

options = ("Rock", "Paper", "Scissors")

# num = random.randint(low, high)  # If you need a random number between 1 and 100
option = random.choice(options)

print(option)
