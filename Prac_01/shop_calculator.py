def main():
    total_price_of_item = 0
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid Number, Try Again")
        number_of_items = int(input("Number of items: "))

    for i in range(1, number_of_items + 1):
        price_of_item = float(input("Price of item: "))
        total_price_of_item += price_of_item

    print("Total price for 3 items is: ${:.2f}".format(total_price_of_item))


main()
