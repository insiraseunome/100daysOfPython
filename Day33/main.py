import os, time

print(r"""                       
|_______|         _              _           _ 
   | | ___   ___ | |  ___       | | (_)  ___| |___ 
   | |/ _ \ / _ \| | / _ \      | | | |/ __|| |
   | | (_) | (_)   || (_) |     | |_| |\__ \| |
   |_|\___/ \___/|_| \___/      |___|_||___/|_|

              Your TO-DO LIST 📝
""")


todoList = []

def printList():
  print()
  for item in todoList:
    print(f"\t➡️\t{item}")
  print("\nHave a nice day!\n")
  time.sleep(3.5)
  os.system("clear")

while True:
  print("\nDo you want to view, add or remove an item from your to do list?")
  menuChoose = input(">> ").lower()
  if menuChoose == "view":
    if todoList:
      printList()
    else:
      print("\n\tEmpty!")
      continue
  elif menuChoose == "add":
    item = input("\n➕\tWhat's next task? >> ").lower()
    todoList.append(item)
    printList()
  elif menuChoose == "remove":
    item = input("\n🗑️\tWhat do you want to remove? >> ").lower()
    if item in todoList:
      todoList.remove(item)
    else:
      print(f"{item} was not in the list")
  else:
    print("\n\t⚠️\tInvalid input. try these options: view / add / remove")
    continue