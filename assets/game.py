import os
import sys
import random
import time
from data import menudata
def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

usr_input = input("> ")
     while (usr_input != 'fish') and (usr_input != 'Exit'):
     usr_input = input("> ")
     if usr_input == 'fish':
        

def shop():
     print("Shop\n"
           "-----------------------------\n"
           "Fish\n"
           "$10\n")
     if usr_input == 'fish':
        print('Item "Fish" was bought')
        wait()
        shop()
     if usr_input == 'Exit':
        game()
def game():
     clear_screen()
     print(""
           "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "                                                       \n"
           "-------------------------------------------------------\n"
           " Shop     |  Exit    |                                 \n"
           "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
     usr_input = input("> ")
     while (usr_input != 'Shop' and 'shop') and (usr_input != 'Exit' and 'exit') and (usr_input != '0'):
         usr_input = input("> ")
     if usr_input == 'Shop' and 'shop':
         shop()
     if usr_input == 'Exit' and 'exit':
         print("Exiting...")
         time.sleep(1)
         clear_screen()
         print(random.choice(menudata.exit))
         sys.exit(1)
