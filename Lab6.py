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

#vigenere_sq()

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

# Part 3

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    if cipher_letter == " ":
        return " "
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    return index_to_letter((cipher_index - key_index) % len(alphabet), alphabet)

def decrypt_vigenere(key, cipher_text, alphabet):
    key_len = len(key)
    resized_key = ""
    plaintext = ""
    for i in range(len(cipher_text)):
        resized_key += key[i % key_len]
        plaintext += undo_vigenere_index(resized_key[i], cipher_text[i], alphabet)
    return plaintext

#plaintext = "THE EAGLE HAS LANDED"
#key = "DAVINCI"
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#encrypted = encrypt_vigenere(key, plaintext, alphabet)
#decrypted = decrypt_vigenere(key, encrypted, alphabet)

#print(f"Encrypted text: {encrypted}")
#print(f"Decrypted text: {decrypted}")


if input("Would you like to use a custom alphabet(Y/N)? ").upper() == "Y":
    alphabet = input("Enter your custom alphabet: ").upper()
else:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = input("Enter your key: ").upper()
while True:
    choice = input("Would you like to (1)Encrypt text, (2)Decrypt text, (3)Quit? ")

    match choice:
        case "1":
            plaintext = input("Enter your plaintext: ").upper()
            print(f"Your encrypted text is: {encrypt_vigenere(key, plaintext, alphabet)}")
        case "2":
            ciphertext = input("Enter your ciphertext: ").upper()
            print(f"Your decrypted text is: {decrypt_vigenere(key, ciphertext, alphabet)}")
        case "3":
            break