<<<<<<< HEAD
def Main():
    
=======
from functions.print_main_menu import print_main_menu
from functions.determine_choice import determine_choice
def main():
    decision = True
    while decision == True:
        choice = print_main_menu()
        decision = determine_choice(choice)

        

main()
>>>>>>> fc91474bcd68c3c9355fb2745ec18d058f5b274d
