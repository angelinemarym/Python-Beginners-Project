from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    cipher_text = ""

    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift)%26
            letter = alphabet[new_position]

        cipher_text += letter
    
    if direction == "encode":
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        print(f"The decoded text is {cipher_text}")

print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    result = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")
    if result == "no":
        should_continue = False
        print('Goodbye')


