import random, os, time

def healthStats(twelveSidedRoll):
  sixSidedRoll = random.randint(1,6)
  return ((sixSidedRoll * twelveSidedRoll) / 2) + 10

def strengthStats(sixSidedRoll):
  twelveSidedRoll = random.randint(1,12)
  return ((twelveSidedRoll * sixSidedRoll) / 2) + 12

def menu():
  while True:
    time.sleep(1)
    print("Welcome to Character Builder 😎\n")
    userName = input("Typo your Legend >> ")
    print("\n")
    typeCharacter = input("Character Type (Human, Elf, Orc, Wizard) >> ")
    health = healthStats(12)
    strength = strengthStats(6)
    print("Welcome to the game,",userName,"the",typeCharacter,"\n")
    print("HEALTH:",health,"\n")
    print("STRENGTH",strength,"\n")
    answer = input("play again? y/n >>")
    if answer == "n":
      break
    elif answer == "y":
      print("yayy\n")
      os.system('clear')
      continue
    else:
      print("y/n , type this input chooses, no invalid typos")
  
menu()