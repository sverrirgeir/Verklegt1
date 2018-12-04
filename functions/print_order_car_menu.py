def print_order_car_menu():
    choice1 = "1. Núverandi Viðskiptavinir"
    choice2 = "2. Nýr Viðskiptavinur"

    print("")
    print("\t{:^10}".format("Pantanir"))
    print("")
    print("\t{:<30}\n\t{:<10}".format(choice1, choice2))
    print("")
    return input("\tValmöguleiki: ")