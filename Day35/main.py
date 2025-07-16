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
  print("\nDo you want to view, add, edit or remove an item from your to do list?")
  menuChoose = input(">> ").lower()
  if menuChoose == "view":
    if todoList:
      printList()
    else:
      print("\n\tEmpty!")
      continue
      else:
        answer = input("Do you want erase the todo list? y/n >> ")
        if answer == 'y':
          todoList.clear()
        else:
          print("ok 😑\n")
          continue
  elif menuChoose == "add":
    item = input("\n➕\tWhat's next task? >> ").lower()
    if not item in todoList: 
      todoList.append(item)
      printList()
    else:
      print(f"{item} already exists!")
  elif menuChoose == "edit":
    item = input("What do you want to edit?\n").lower()
    newItem = input("What do you want to change it to?\n").lower()
    for i in range(0,len(todoList)):
      if todoList[i] == item:
        todoList[i] = newItem
        print(f"Alright! Your new task is: {newItem}\n")
        printList()
      else:
        print(f"{item} already exists!")
  elif menuChoose == "remove":
    item = input("\n🗑️\tWhat do you want to remove? >> ").lower()
    if item in todoList:
      print(f"\n{item}")
      answer = input("\nAre you sure you want to remove this? y/n >> ").lower()
      if answer == 'y':
        todoList.remove(item)
        print(f"{item} removed")
      else:
        print(f"ok. {item} will continue in the list")
    else:
      print(f"{item} was not in the list")
  else:
    print("\n\t⚠️\tInvalid input. try these options: view / add / edit / remove")
    continue