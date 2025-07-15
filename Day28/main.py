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
    
    userNameOne = input("Typo your Legend >> ")
    print("\n")
    characterOne = input("Character Type (Human, Elf, Orc, Wizard) >> ")
    healthPlayerOne = healthStats(12)
    strengthPlayerOne = strengthStats(6)
    print("Welcome to the game,",userNameOne,"the",characterOne,"\n")
    print("HEALTH:",healthPlayerOne,"\n")
    print("STRENGTH",strengthPlayerOne,"\n\n")
    print("Who are they battling?\n")
    userNameTwo = input("Typo your Legend >> ")
    print("\n")
    characterTwo = input("Character Type (Human, Elf, Orc, Wizard) >> ")
    healthPlayerTwo = healthStats(12)
    strengthPlayerTwo = strengthStats(6)
    print("Welcome to the game,",userNameTwo,"the",characterTwo,"\n")
    print("HEALTH:",healthPlayerTwo,"\n")
    print("STRENGTH",strengthPlayerTwo,"\n")
    print(userNameOne,"the",characterOne,"⚔️ VS ⚔️",userNameTwo,"the",characterTwo)
    print("OK, LET'S GET STARTEEED!!!")
    time.sleep(1)
    os.system("clear")
    rounds = 0
    while True:
      print("⚔️ Go to mortal battle!! ⚔️")
      playerOneToRoll = random.randint(1,6)
      playerTwoToRoll = random.randint(1,6)
      time.sleep(1)
      print("Player one rolled:", playerOneToRoll,"\n")
      print("Player two rolled:", playerTwoToRoll,"\n")
      if(playerOneToRoll > playerTwoToRoll):
        print(userNameOne,"win this round!")
        damage = max(5, (strengthPlayerOne - strengthPlayerTwo) + 1)
        print(damage, "\033[91m damage!! \033[0m")
        healthPlayerTwo -= damage
        print("Player two Health:", healthPlayerTwo,"\n")
        rounds += 1
        print("Go to round", rounds,"!!!\n")
        time.sleep(2)
        os.system("clear")
        if healthPlayerTwo <= 0:
          print("⚔️",userNameOne,"win this dangerous battle!! ⚔️\n")
          print(userNameOne,"destroyed",userNameTwo,"in",rounds,"rounds!! impressive!")
          break
      elif(playerOneToRoll < playerTwoToRoll):
        print(userNameTwo,"win this round!")
        damage = max(5, (strengthPlayerTwo - strengthPlayerOne) + 1)
        print(damage, "\033[91m damage!! \033[0m")
        healthPlayerOne -= damage
        print("Player one Health:", healthPlayerOne,"\n")
        rounds += 1
        print("Go to round", rounds,"!!!\n")
        time.sleep(2)
        os.system("clear")
        if healthPlayerOne <= 0:
          print("⚔️",userNameTwo,"win this dangerous battle!! ⚔️\n")
          print(userNameTwo,"destroyed",userNameOne,"in",rounds,"rounds!! impressive!")
          break
      else:
        print("Tie! play again...")
        continue
        
    playAgain = input("Do you want to play again? (y/n): ").lower()
    if playAgain != 'y':
        break
menu()