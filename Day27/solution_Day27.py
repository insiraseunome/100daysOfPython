"""
👉 Day 27 Challenge
Welcome to your first video game creation. You will create a video game that creates a character's health 
and attack stats...along with an epic name for your character.

Do not delete today's code. You will be building upon it on Day 28.

Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, 
etc.).
Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health 
stats. Use this formula:

(6-sided-roll * 12-sided-roll) / 2 + 10

Write a second subroutine that multiplies a bunch of random dice rolls together to generate the character's 
strength stats. Use this formula:

(6-sided-roll * 12-sided-roll) / 2 + 12

Present the data in a menu with time.sleep and os.system("clear") to make it appealing.
Wrap it in a loop so the user has the option to create another character.
"""

import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

while True:
  print("⚔️ CHARACTER BUILDER ⚔️")
  print()
  name = input("Name your Legend:\n")
  type = input("Character Type (Human, Elf, Wizard, Orc):\n")
  print()
  print(name)
  print("HEALTH:", health())
  print("STRENGTH:", strength())
  print()
  print("May your name go down in Legend…")
  print()
  again = input("Again?:\n")
  if again=="No" or again=="no":
    break
  time.sleep(1)
  os.system("clear")