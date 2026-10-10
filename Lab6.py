# Part 1 - Printing the Vigenere Square

def vigenere_sq():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f"|---|", end="")
    for letter in alphabet:
        print(f"| {letter} ", end ="")
    print(f"")
    for _ in range(108):
        print(f"=", end="")
    print(f"")
    shifted = alphabet
    for i in range(25):
        print(f"| {alphabet[i]} |", end="")
        for letter in shifted:
            print(f"| {letter} ", end="")
        shifted = shifted[1:] + shifted[0]
        print(f"")

vigenere_sq()

# Part 2 - Encryption

def letter_to_index(letter, alphabet):
    index = 0
    for character in alphabet:
        if character == letter:
            return index
        index += 1
    print(f"Letter {letter} not found in alphabet {alphabet}")
    return -1

def index_to_letter(index, alphabet):
    return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    if plaintext_letter == " ":
        return " "
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    return index_to_letter((key_index + plaintext_index) % len(alphabet), alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    key_len = len(key)
    resized_key = ""
    ciphertext = ""
    for i in range(len(plaintext)):
        resized_key += key[i % key_len]
        ciphertext += vigenere_index(resized_key[i], plaintext[i], alphabet)
    return ciphertext

plaintext = "THE EAGLE HAS LANDED"
key = "DAVINCI"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(encrypt_vigenere(key, plaintext, alphabet))
