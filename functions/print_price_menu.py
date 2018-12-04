from Verklegt1.Main import main
def print_price_menu():
    """Prints out the main menu and returns a input sentence asking for a choice"""
    insure = "Aukatrygging 30.000kr"
    choice1 = "Smábílar"
    price1 = "10.000kr"
    choice2 = "Fólksbílar"
    price2 = "15.000kr"
    choice3 = "Jeppar"
    price3 = "20.000kr"
    choice4 = "Húsbílar"
    price4 = "25.000kr"
    over100 = "Athugið dagverð miðast við 100 ekna km á dag að meðaltali yfir \n leigutíma. Gjald fyrir akstur umfram 100 km miðast við 1% \n af dagverði fyrir hvern kílómetra umfram 100km"
    print("")
    print("\t{:^10}".format("Bílaleiga ehf"))
    print("")
    print("================================================================")
    print("")
    print("\t{:<10}\t{:^10}\t{:^10}".format("Flokkur","Verð","Trygging"))
    print("")
    print("----------------------------------------------------------------")
    print("")
    print("\t{:<10}\t{:^10}\t{:^10}".format(choice1,price1,insure))
    print("")
    print("----------------------------------------------------------------")
    print("")
    print("\t{:<10}\t{:^10}\t{:^10}".format(choice2,price2,insure))
    print("")
    print("----------------------------------------------------------------")
    print("")
    print("\t{:<10}\t{:^10}\t{:^10}".format(choice3,price3,insure))
    print("")
    print("----------------------------------------------------------------")
    print("")
    print("\t{:<10}\t{:^10}\t{:^10}".format(choice4,price4,insure))
    print("")
    print("----------------------------------------------------------------")
    print("")
    print(over100)
    print("")
    print("================================================================")
    print("")
    print("\t{:<30}\n\t{:<10}".format("1. Prenta út Verðlista","2. Til baka"))
    print("")
    val = input("\tValmöguleiki: ")
    print(val)
    main()
        
    return 