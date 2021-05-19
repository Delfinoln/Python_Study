# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

# Importing data_frame
data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

for (index, rows) in data_frame.iterrows():
    print(rows)