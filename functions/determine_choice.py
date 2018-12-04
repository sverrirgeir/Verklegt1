from functions.print_order_menu import print_order_menu
from functions.print_clients_menu import print_clients_menu
from functions.print_car_menu import print_car_menu
from functions.print_price_menu import print_price_menu
from functions.print_order_car_menu import print_order_car_menu

def determine_choice(choice):
    if choice == "1":
        print_order_menu()
    elif choice == "2":
        print_clients_menu()
    elif choice == "3":
        print_car_menu()
    elif choice == "4":
        print_price_menu()
    elif choice == "5":
        print_order_car_menu()
    else:
        return False