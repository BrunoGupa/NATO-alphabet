import pandas as pd

nato_alph = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dic = {row.letter: row.code for (index, row) in nato_alph.iterrows()}


def generate_input():
    word = input("Type a word: ")
    my_list = [letter for letter in word]
    try:
        phonetic_list = [nato_dic[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry. Nato Alphabet only accepts letters")
        generate_input()
    else:
        print(phonetic_list)


generate_input()
