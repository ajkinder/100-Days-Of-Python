# Caesar's Cipher
# Code and Decode messages using Caesar's Cipher
# Written by: Alexander Kinder

# IMPORTS
import art

# GLOBAL VARIABLES
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# MARK - Function declarations
def caesar(input_text, shift_by, cipher_direction):
    return_message = ""
    if cipher_direction == "decode":
        shift_by *= -1

    for letter in input_text:
        if letter in alphabet:
            return_message += alphabet[alphabet.index(letter) + shift_by]
        else:
            return_message += letter

    print(f"The {cipher_direction}d text is {return_message}")


# BODY
print(art.logo)

is_running = True

while is_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # adjustment for large shift inputs

    caesar(input_text=text, shift_by=shift, cipher_direction=direction)

    play_input = input("\nDo you want to encode or decode another message?\n").lower()
    if play_input == "no":
        is_running = False
        print("Goodbye!")
