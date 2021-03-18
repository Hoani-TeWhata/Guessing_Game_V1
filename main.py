target = 50 

guess = int(input("Please guess the number: "))



if guess == target:
  print("Congratulations! You got the number")
elif guess < target:
  print("Your guess was too low")
elif guess > target:
  print("Your guess was too high")
else:
  print("Something went wrong")  