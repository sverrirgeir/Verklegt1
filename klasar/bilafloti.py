def allcars():
    with open("cars.txt", "r") as f:
        for text in f:
            all_cars = text.split(",")
            print(all_cars)
    return

allcars()