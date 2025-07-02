import random

def rollDice(side):
  diceWith_sides = random.randint(1, side)
  return diceWith_sides

print("⚔️ Character Stats Generator ⚔️\n")
colors = [
  "\033[91m",
  "\033[92m",
  "\033[93m",
  "\033[94m",
  "\033[95m",
  "\033[96m",
  "\033[97m"
]
reset = "\033[0m"

while True:
  userName = input("Name your warrior: ")
  sixSides = rollDice(6)
  eightSides = rollDice(8)
  totalHP = sixSides * eightSides
  color = random.choice(colors)
  print(color,"Their health is:",totalHP,"hp",reset)
  answer = input("continue? y/n >> ")
  if answer == "n":
    print("ok. bye")
    break


""" cores em python

033[30m  Preto
033[31m  Vermelho
033[32m  Verde
033[33m  Amarelo
033[34m  Azul
033[35m  Magenta
033[36m  Ciano
033[37m  Branco

033[90m  Preto claro (cinza escuro)
033[91m  Vermelho claro
033[92m  Verde claro
033[93m  Amarelo claro
033[94m  Azul claro
033[95m  Magenta claro
033[96m  Ciano claro
033[97m  Branco brilhante

033[0m para resetar a cor no final da string
"""