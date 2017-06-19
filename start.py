try:
     import sys
     import os
     import time
     import random
     from data import *
 except ImportError:
         print("sys or os was not found!")
          
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")        
def user_choice():
    return input("> ").lower().strip()
def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")
          
def menu():
     print("-=-=-=-=-=-=-=-=-=-=\n"
           "     Aquarium\n"
           "An awesome !!FISH!! game"
           "-=-=-=-=-=-=-=-=-=-=\n")
     print("1. Start\n"
           "\n"
           "2. Credits\n"
           "\n"
           "0. Exit")
     choice = user_choice
     if choice == "1":
          print("Loading...")
          time.sleep(5)
          
     if choice == "2":
          print("Credits -\n"
                "\n"
                "Project manager:\n"
                "DRAGONBLOOD830\n"
                "Developers\n"
                "Articuno1234")
          wait()
          menu()
     if choice == "0":
          print("Exiting...")
          time.sleep(1)
          sys.exit(1)
