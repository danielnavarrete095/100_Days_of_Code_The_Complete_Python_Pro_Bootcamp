import pandas
DATA_FILE = "nato_phonetic_alphabet.csv"
def main():
    data_frame = pandas.read_csv(DATA_FILE)
    data_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}
    # print(data_dict)
    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    is_on = True
    while(is_on):
        user_word = input("Enter a word: ")
        word_list = [letter.upper() for letter in user_word if letter.isalpha()]
        nato_list = [data_dict[letter] for letter in word_list]
        print(nato_list)

if __name__ == '__main__':
    main()


