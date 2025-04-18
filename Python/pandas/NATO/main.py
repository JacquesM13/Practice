import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("What word would you like to spell in phonetics? ").upper()

nato_word = [nato_dict[letter] for letter in word]

print(nato_word)