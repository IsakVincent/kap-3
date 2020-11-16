import random

number = random.randint(1, 10)
guesses = 0
guess = 0

while guess != number:
  guesses += 1
  guess = int(input("Gissa på ett heltal(int) mellan 1 och 10: "))

  if guess < number:
    print(f"Din gissning {guess} är för liten.")
  elif guess > number:
    print(f"Din gissning {guess} är för stor.")

print(f"Grattis du klarade det på {guesses} gissnigar! ")