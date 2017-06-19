try:
     import sys
     import os
     import time
     import random
     from data import coins
     from data import menudata
     from assets import game
except ImportError:
         print("sys or os was not found!")
          
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

def sig_handler(signal, frame):
    print("\nExiting...")
    time.sleep(1)
    clear_screen()
    print(random.choice(menudata.exit))
    sys.exit(0)
def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
def credits():
     clear_screen()
     print("Credits -\n"
           "\n"
           "Project manager:\n"
           "DRAGONBLOOD830\n"
           "Developers\n"
           "Articuno1234")
     wait()
     menu()
def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")
          
def menu():
     clear_screen()
     print("-=-=-=-=-=-=-=-=-=-=\n"
           "     Aquarium\n"
           "An awesome !!FISH!! game\n"
           "-=-=-=-=-=-=-=-=-=-=\n")
     print("1. Start\n"
           "\n"
           "2. Credits\n"
           "\n"
           "0. Exit")
     usr_input = input("> ")
     while (usr_input != '1') and (usr_input != '2') and (usr_input != '0'):
         usr_input = input("> ")
     if usr_input == '1':
         game.game()
     if usr_input == '2':
         credits()
     if usr_input == '0':
         print("Exiting...")
         time.sleep(1)
         clear_screen()
         print(random.choice(menudata.exit))
         sys.exit(1)

menu = menu()
print(menu)
