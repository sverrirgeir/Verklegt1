from functions.print_main_menu import print_main_menu
from functions.determine_choice import determine_choice
from functions.print_clients_menu import print_clients_menu
from functions.print_car_menu import print_car_menu
from functions.print_price_menu import print_price_menu
from functions.print_order_car_menu import print_order_car_menu
def main():
    decision = True
    while decision == True:
        choice = print_main_menu()
        decision = determine_choice(choice)

        

main()