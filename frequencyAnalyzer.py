#!/usr/local/bin/python3

# kleinste und höchste Nummer des möglichen Buchstabens für das jeweilige Verfahren
lowest = int(input("Lowest ASCII number: "))
highest = int(input("Highest ASCII number: "))

# der Text, welcher analysiert werden soll
text = input("Text to analyze: ")

# Liste aller möglichen Zeichen
characters = [chr(i) for i in range(lowest, highest+1)]

# zählt wie viel Mal der Buchstabe, die Ziffer oder das Sonderzeichen im Text vorkommt
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

# rechnet es in Prozent um und gibt das Resultat visualisiert im Commandprompt zurück
def percentage():
    zeroPerc = []
    for char in characters:
        perc = 100 * count_char(text, char) / len(text)
        # zeigt nur die relevanten an
        if perc == 0:
            zeroPerc.append(char)
        elif perc != 0:
            print("{0} - {1} %".format(char, round(perc, 2)))

    print(f"{zeroPerc} - 0.0 %\n")

percentage()
