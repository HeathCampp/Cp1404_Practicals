number_1 = int(input("Enter in number > "))
number_2 = int(input("Enter in number > "))
number_3 = int(input("Enter in number > "))
number_4 = int(input("Enter in number > "))
number_5 = int(input("Enter in number > "))

count = 0
lists = [number_1, number_2, number_3, number_4, number_5]
for number in lists:
    print("Number: {}".format(lists[count]))
    count += 1

first_number = lists[0]
print("The first number is {}".format(first_number))

last_number = lists[-1]
print("The last number is {}".format(last_number))

smallest_number = min(lists)
print("The smallest number is {}".format(smallest_number))

largest_number = max(lists)
print("The largest number is {}".format(largest_number))

average_number = sum(lists)
print(average_number/count)


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob', '*']
username = input("Enter in username > ")
if username in usernames:
    print("Access denied")
if username not in usernames:
    print("Access granted")