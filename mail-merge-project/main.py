#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from pathlib import Path
PATH_SCRIPT = str(Path(__file__).parent.absolute())
REL_PATH_LETTER = r"\Input\Letters\starting_letter.txt"
REL_PATH_NAMES = r"\Input\Names\invited_names.txt"
REL_PATH_RDY = r"\Output\ReadyToSend\\"
PATH_TO_LETTER = PATH_SCRIPT + REL_PATH_LETTER
PATH_TO_NAMES = PATH_SCRIPT + REL_PATH_NAMES
PATH_TO_READY = PATH_SCRIPT + REL_PATH_RDY
def main():
    starting_text = ""
    names_list = []
    with open(PATH_TO_LETTER, 'r') as file:
        starting_text = file.read()
        print(starting_text)
    with open(PATH_TO_NAMES, 'r') as file:
        names = file.readlines()
        print(names)
    for name in names:
        new_name = name.replace('\n', '')
        new_text = starting_text.replace("[name]", new_name)
        letter_name = f"Letter_for_{new_name}.txt"
        with open(PATH_TO_READY + letter_name, 'w') as file:
            file.write(new_text)
if __name__ == '__main__':
    main()