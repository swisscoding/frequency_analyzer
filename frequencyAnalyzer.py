#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Text analyzer | ----\n", fg("red")))

# functions
# counts every character
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

# returns in percentage
def percentage():
    zeroPerc = []
    for char in characters:
        perc = 100 * count_char(text, char) / len(text)
        if perc == 0:
            zeroPerc.append(char)
        elif perc != 0:
            print("{0} - {1} %".format(char, round(perc, 2)))

    print(f"{zeroPerc} - 0.0 %\n")

# user interaction
lowest = int(input("Lowest ASCII number: "))
highest = int(input("Highest ASCII number: "))
text = input("Text to analyze: ")

# all characters in interval
characters = [chr(i) for i in range(lowest, highest+1)]

# main execution
percentage()
