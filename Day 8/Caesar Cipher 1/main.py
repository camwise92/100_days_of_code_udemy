alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):
    encrypted_sentence = []
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + shift_amount
            if new_index > 25:
                new_index =
            new_letter = alphabet[new_index]
            encrypted_sentence.append(new_letter)
        if letter == " ":
            new_letter = letter
            encrypted_sentence.append(new_letter)
    return "".join(encrypted_sentence)


print(encrypt(text, shift))


