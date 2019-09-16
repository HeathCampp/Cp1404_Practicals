"""..."""

from Prac_06.Guitar_exercise import Guitar

guitars = []
banjo = Guitar("banjo", 1922, 20000.50224)
guitar_2 = Guitar("guitar_2", 2000, 2345)
guitar_3 = Guitar("guitar_3", 1800, 2345)
guitar_4 = Guitar("guitar_4", 2250, 2345)
guitar_5 = Guitar("guitar_5", 2060, 2345)
guitar_6 = Guitar("guitar_6", 1246, 2345)
guitars.append(banjo)
guitars.append(guitar_2)
guitars.append(guitar_3)
guitars.append(guitar_4)
guitars.append(guitar_5)
guitars.append(guitar_6)


print("guitar tracker v1.0")

choice = input("enter choice: ").lower()
while choice != "":
    if choice == "a":
        print("add a guitar")
        guitar_name = input("name: ")
        year = int(input("year: "))
        cost = float(input("cost:"))
        guitar_name = Guitar(guitar_name, year, cost)
        guitars.append(guitar_name)
        print(guitar_name, "Added")
    elif choice == "l":
        # TODO: figure out sequence iteration for lists of objects
        # name_format = max([len(guitar) for guitar in guitars])
        for i, guitar in enumerate(guitars):
            vintage = ""
            if guitar.is_vintage():
                vintage = " vintage"
            print("Guitar {}: {:10} ({:>4}), worth $ {:.2f}{:<}".format(i, guitar.name, guitar.year, guitar.cost,
                                                               vintage))
    else:
        print("wrong input")
    choice = input("enter choice: ").lower()
