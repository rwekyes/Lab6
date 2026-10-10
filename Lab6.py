# Part 1 - Printing the Vigenere Square

def vigenere_sq():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f"|---|", end="")
    for letter in alphabet:
        print(f"| {letter} ", end = "")
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

