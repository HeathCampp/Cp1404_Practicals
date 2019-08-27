# Part 1
def main():
    username = input("What is your name?: ")
    name_file = open("Name.txt", 'w')
    name_file.write(username)
    name_file.close()

# Part 2
    in_name_file = open("Name.txt", 'r')
    username = in_name_file.read()
    print("Your name is {}".format(username))
    in_name_file.close()


# Part 3
    name_file = open("Number_file.txt", 'w')
    name_file.write("17\n42")
    name_file.close()

    in_name_file = open("Number_file.txt", 'r')
    total = 0
    for new_line in in_name_file:
        total += int(new_line)
    in_name_file.close()
    print(total)


main()

