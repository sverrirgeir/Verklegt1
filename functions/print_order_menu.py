def print_order_menu():
    choice1 = "1. Skrá nýja pöntun"
    choice2 = "2. Leita af pöntun"
    choice3 ="3. Pöntunarlisti"
    choice4 ="4. Til baka"

    print("")
    print("\t{:^10}".format("Pantanir"))
    print("")
    print("\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4))
    print("")
    return input("\tValmöguleiki: ")