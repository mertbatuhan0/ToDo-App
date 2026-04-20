import os
from sys import excepthook

print("welcome the To Do List Application")
print("-----------------------------")
Duties = []
def add_duty():
    adding_duty = input()
    Duties.append(adding_duty)

def remv_duty():
    print("which duty do you want to remove")
    try:
        selected_duty = int(input())
        Duties.pop(selected_duty)
    except ValueError:
        print( "Please enter a valid duty number")
def show_duties():
    if len(Duties) == 0:
        print("No duties , please add duty")
    else:
        for Duty in Duties:
            print(Duty)

def exit_program():
    exit()

while True:
    print("1. Add duty")
    print("2. Remove duty")
    print("3. Show duties")
    print("4. Exit")


    choice = input()
    if choice == "1":
        add_duty()
        print("your duty has been added")
    elif choice == "2":
        remv_duty()
        print("your duty has been removed")
    elif choice == "3":
        show_duties()
        print("your duty has been displayed")
    elif choice == "4":
        print("Exit , See you next time :)")
        break
    else :
        print("Please enter your choice")


