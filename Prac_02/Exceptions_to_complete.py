"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
result = 0
finished = False
while not finished:
    try:
        result = int(input("Answer in any integer: "))
        finished = True

    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", result)
