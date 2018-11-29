""" Simple implementation of both encryption and decryption of the vigenere algo """

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt():
    c = ""
    print("Please enter your text: ")
    plaintext = input()
    plaintext = plaintext.lower()
    print("Enter your key: ")
    key = input()

    plaintext = plaintext.replace(' ','')
    repeating_key = ""
    while len(repeating_key)<len(plaintext):
        repeating_key += key

    # shrink the key to the size of the plaintext
    repeating_key = repeating_key[:len(plaintext)]

    # make character comparisons
    for i in range(len(plaintext)):
        x = ord(plaintext[i])-97            # returns the ascii value of i in p
        print(x)
        y = ord(repeating_key[i])-97        # returns the ascii value of i in k
        print(y)
        z = abs(x+y)%26
        print(z)
        c+=alphabet[z]

    return c

def decrypt():
    p = ""
    print("Please enter your ciphertext: ")
    ciphertext = input()
    ciphertext = ciphertext.lower()
    print("Enter your key: ")
    key = input()

    ciphertext = ciphertext.replace(' ','')
    repeating_key = ""
    while len(repeating_key)<len(ciphertext):
        repeating_key += key

    # shrink the key to the size of the plaintext
    repeating_key = repeating_key[:len(ciphertext)]

    # make character comparisons
    for i in range(len(ciphertext)):
        x = alphabet.index(ciphertext[i])            # returns the ascii value of i in c
        print(x)
        y = alphabet.index(repeating_key[i])        # returns the ascii value of i in k
        print(y)
        if x<y:
            x+=26
        z = abs(x-y)
        print(z)
        p+=alphabet[z]

    return p

if __name__ == '__main__':
    print("Enter the corresponding number for the task you wish to run:\n1) Encrypt\n2) Decrypt\n")
    while True:
        try:
            ans = int(input())
            print("Answer:", type(ans))
            if ans == 1:
                c = encrypt()
                print(c)
                break
            elif ans == 2:
                print("about to run decrypt")
                p = decrypt()
                print(p)
                break
            else:
                print("Please enter 1 or 2.")
        except:
            print("Please enter a valid number")
