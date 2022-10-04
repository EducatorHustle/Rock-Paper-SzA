import random

print("*******Play Name**********")
player1 = "The Bot"
player2 = input(" Enter your Name: ")


def choice():
  n = random.randint(1, 3)
  return n


def display(n):
  if n == 1:
    print("Rock")
  elif n == 2:
    print("Paper")
  else:
    print("Scissors")


def validate(p):  #Validation
  if p.isnumeric():
    if int(p) >= 1 and int(p) <= 3:
      return True
    else:
      return False
  else:
    return False


play = "Yes"
while play[0] != "n":
  p2 = input("1.Rock 2.Paper 3. Scissors (1,2 or 3): ")  #Validation
  while not validate(p2):
    p2 = input("Invalid. \n1.Rock 2.Paper 3. Scissors (1,2 or 3): ")
    print(player2, end=": ")
  p2 = int(p2)
  display(p2)
  print(player1, end=": ")
  p1 = choice()
  display(p1)
  if p1 == p2:
    print("Draw")
  elif p1 == 1 and p2 == 3:
    print(player1, "wins")
  elif p1 == 2 and p2 == 1:
    print(player1, "wins")
  elif p1 == 3 and p2 == 2:
    print(player1, "wins")
  else:
    print(player2, "wins")

  play = input("Play again? (y/n): ")
