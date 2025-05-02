"""
Write a Python program that takes a list of numbers and counts how many times each number appears using a dictionary. Then print the frequency of each number.

"""

haxtable = {}

lists = [1, 2, 3, 4, 3, 2, 5, 3, 8, 19, 34, 24]

for i in lists:
    if i in haxtable:
        haxtable[i] += 1
    else:
        haxtable[i] = 1

for key in haxtable:
    print(f"key appears {key}, in {haxtable[key]} Times")