MIN_LENGTH = 2
MAX_LENGTH = 6


def main():
    password = get_password()
    password = is_valid_password(password)
    print("Your {} - character password is valid:".format(len(password)))
    print("Your password is: {}".format(convert_to_asterisks(password)))


def get_password():
    password = input("Enter Password: ")
    valid_password = False
    while valid_password is False:
        if 2 < len(password) < 6:
            valid_password = True
        else:
            print("Invalid password!")
            password = input("Enter Password: ")
    return password


def convert_to_asterisks(password):
    asterisks = len(password) * "*"
    return asterisks


def is_valid_password(password):
    count_digit = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
    return password


main()
