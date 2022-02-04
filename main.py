# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

nato_alph = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dic = {row.letter: row.code for (index, row) in nato_alph.iterrows()}
#print(nato_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Type a word ")
my_list = [letter for letter in word]
phonetic_list = [nato_dic[letter.upper()] for letter in word]
print(phonetic_list)

