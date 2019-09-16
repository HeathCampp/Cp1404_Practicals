numbers = [3, 1, 4, 1, 5, 9, 2]
# number[0] = 3
# number[-1] = 2
# number[3] = 1
# number[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = True
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1.
numbers[0] = 10
print(numbers)

# 2.
numbers[-1] = 1
print(numbers)

# 3.
element = numbers[2:]
print(element)

# 4.
key = 9 in numbers
print(key)

