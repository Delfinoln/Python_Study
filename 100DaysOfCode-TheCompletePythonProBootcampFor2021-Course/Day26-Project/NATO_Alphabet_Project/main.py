#TODO 1. Create a dictionary in this format:

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

# Importing data_frame
data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

# Creating a dictionary of the letters and each corresponding code
nato_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

# Creating a list of the phonetic code words from a word that the user inputs.
user_answer = input("Enter a word: ").upper()
nato_list = [nato_dict[letter] for letter in user_answer]

print(nato_list)
