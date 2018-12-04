
def print_main_menu():
    """Prints out the main menu and returns a input sentence asking for a choice"""
    choice1 = "1. Pantanir"
    choice2 = "2. Viðskiptavinir"
    choice3 = "3. Bílar"
    choice4 = "4. Verðlisti"
    choice5 = "5. Panta bíl"
    choice6 = "6. Hætta"
    print("")
    print("\t{:^10}".format("Bílaleiga ehf"))
    print("")
    print("\t{:<30}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}\n\t{:<10}".format(choice1, choice2, choice3, choice4, choice5, choice6))
    print("")
    return input("\tValmöguleiki: ")