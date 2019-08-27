for i in range(1, 21, 2):
    print(i, end=' ')
print()

# part a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# part b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# part c
user_number = int(input("Please enter in a number: "))
for i in range(1, user_number + 1, 1):
    print('*', end=' ')
print()

# part d
for i in range(1, user_number + 1):
    print('*' * i)
