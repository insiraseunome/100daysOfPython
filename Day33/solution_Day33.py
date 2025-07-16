"""
👉 Day 33 Challenge
Create your own to do list manager. (This can be super useful!)

Ask the user whether they want to view, add, or edit their to do list.
If they want to view it, print it out in a nice way (Hint: subroutine).
If they choose to add an item to the to do list, allow them to type in the item and then add it to the bottom of the list.
If they want to edit the to do list, ask them which item they completed, and remove it from the list.
Don't worry about duplicates!
The first item you put in the list should be the first item you remove.
Add a title, some color, alignment to the text, or emojis. Show off your skills!
"""

import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu=="edit":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)