"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?: When you type in anything that's not an integer, for example,string
2. When will a ZeroDivisionError occur?: When you divide by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, if you make sure the denominator
cannot be 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

