# Caesar's Cipher
# Code and Decode messages using Caesar's Cipher
# Written by: Alexander Kinder

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# MARK - Function declarations
def encrypt(plain_message, shift_by):
    encoded_message = ""
    for letter in plain_message:
        encoded_message += alphabet[alphabet.index(letter) + shift_by]
    print(f"The encrypted text is {encoded_message}")


def decrypt(cypher_message, shift_by):
    decoded_message = ""
    for letter in cypher_message:
        decoded_message += alphabet[alphabet.index(letter) - shift_by]
    print(f"The decrpted text is {decoded_message}")


if direction == "encode":
    encrypt(plain_message=text, shift_by=shift)
elif direction == "decode":
    decrypt(cypher_message=text, shift_by=shift)

