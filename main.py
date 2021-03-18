import random

target= random.randint(1,100)

guess = int(input("Please guess the number: "))


if guess == target:
  print("Congratulations! You got the number")
elif guess < target:
  print("Your guess was too low")
elif guess > target:
  print("Your guess was too high")
else:
  print("Something went wrong")  
