"""
week 6 lecture pracs
01. lecture warm-up

"""

INDEX_ON_SALE = 2


def main_01():
    """List comprehension finding only products that are on sale"""
    # products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True], ["HDMI Cable", 10, False]]
    # on_sale_products = [product[0] for product in products if product[INDEX_ON_SALE]]

    products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True), Product("HDMI Cable", 10, False)]
    on_sale_products = [product for product in products if product.is_on_sale]
    print(on_sale_products)

class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = ""
        if self.is_on_sale:
            on_sale_string = " ON SALE!"
        return "{} ${:.2f}{}".format(self.name, self.price, on_sale_string)

    def __repr__(self):
        return str(self)


main_01()
