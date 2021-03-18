import random

target= random.randint(1,100)

guess = int(input("Please guess the number: "))

while guess != target: 

 
 if guess < target:
  print("Your guess was too low")
 elif guess > target:
  print("Your guess was too high")
 guess = int(input("Please guess the number: "))



print("Congratulations! You got the number!")