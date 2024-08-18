import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def gen_phonetic_letters():
    user_input = input("Enter a word-> ").upper()
    try:
        word_code = [phonetic_dict[word] for word in user_input]
    except KeyError:
        print("Sorry, only English alphabet accepted")
    else:
        print(word_code)
    finally:
        gen_phonetic_letters()


gen_phonetic_letters()
