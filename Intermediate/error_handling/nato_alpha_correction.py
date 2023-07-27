import pandas

nato_df = pandas.read_csv(
    "NATO_alphabet_project/nato_alphabet_project/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

print(nato_dict)


def generate_nato():
    user_input = input("Enter a word ").upper()
    try:
        user_list = [nato_dict[let] for let in user_input]
    except KeyError:
        print("Please Enter only letters")
        generate_nato()
    else:
        print(user_list)


generate_nato()
