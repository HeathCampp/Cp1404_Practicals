"""
Write a program to count the occurrences of words in a string.
The program should ask the user for a string, then print the counts of how many of each word are in the file.
"""

new_words = input("Text: ").split()
count_words = {}
for word in new_words:
    if word in count_words:
        count_words[word] += 1
    else:
        count_words[word] = 1

new_words = list(count_words.keys())
new_words.sort()

for word in new_words:
    print("{} : {}".format(word, count_words[word]))
