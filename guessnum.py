#Python number guessing game
import random

lowest_num = 10
highest_num = 1000
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True
print("Python Number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running : 

  guess = input("Enter your guess:")

  if guess.isdigit():
      guess = int(guess)
      guesses += 1

      if guess < lowest_num or guess > highest_num:
       print("That is out of random number")
       print(f"pls select a number Select a number between {lowest_num} and {highest_num}")
      elif guess < answer:
        print("too Low! try again ")
      elif guess > answer:
        print("too High! try again")
      else:
        print(f"Correct! The answer was {answer}")
        print(f"Number of guesses: {guesses}")
        is_running = False
  else:
    print("Invalid guess")
    print(f"pls select a number Select a number between {lowest_num} and {highest_num}")
