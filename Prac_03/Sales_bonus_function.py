"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    user_bonus = 0
    sales = float(input("Enter sales: $"))
    print(determine_sale_price(sales))
    print(user_bonus)


def determine_sale_price(sales):
    if sales < 1000:
        user_bonus = (sales * 0.1)
        return user_bonus
    elif sales >= 1000:
        user_bonus = sales * 0.15
        return user_bonus


main()
