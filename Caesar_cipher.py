logo = '''
   _____                                  _____  _         _                 
  / ____|                                / ____|(_)       | |                
 | |      __ _   ___  ___   __ _  _ __  | |      _  _ __  | |__    ___  _ __ 
 | |     / _` | / _ \/ __| / _` || '__| | |     | || '_ \ | '_ \  / _ \| '__|
 | |____| (_| ||  __/\__ \| (_| || |    | |____ | || |_) || | | ||  __/| |   
  \_____|\__,_| \___||___/ \__,_||_|     \_____||_|| .__/ |_| |_| \___||_|   
                                                   | |                       
                                                   |_|                       
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    cipher_text = ""
    for text_letter in text:
        not_in_alphabet = True
        for idx, alphabet_letter in enumerate(alphabet):
            if text_letter == alphabet_letter:
                not_in_alphabet = False
                alphabeth_size = len(alphabet)
                if shift > alphabeth_size:
                    shift = shift % alphabeth_size
                if direction == "encode" or direction == "encrypt":
                    final = len(alphabet) - 1
                    dest = idx + shift
                    index = dest if not dest > final else dest - final - 1
                    cipher_text += alphabet[index]
                elif direction == "decode" or direction == "decrypt":
                    dest = idx - shift
                    cipher_text += alphabet[dest]
        if not_in_alphabet:
                cipher_text += text_letter

    print(f"Here's the encoded result: {cipher_text}")

end = False
print(logo)
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    answer = input('Type "yes" if you want to go again, otherwise type "no"\n').lower()
    if answer == "yes" or answer == "y":
        continue
    else:
        print("Good bye!")
        break