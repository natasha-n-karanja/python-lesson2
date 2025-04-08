import random

secret_number = random.randint(1, 20)
attempts = 5

print("🎮 Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 20.")
print(f"You have {attempts} attempts. Good luck! \n")

while attempts > 0:
  guess = int(input("Enter your guess: "))
  if guess == secret_number:
    print("🎉 Congrats! You guessed it right!")
    break
  elif guess < secret_number:
    print("Too low!")
  else:
    print("Too high!")
  
  attempts -= 1
  print(f"Attempts left: {attempts} \n")

  if attempts == 0:
    print(f"😞You're out of attempts. The number was {secret_number}. Better luck Better luck next time! next time!")