# key generation p,g,a
# A = g^a(mod)p

p = 29
g = 5
A = None
a = 3

def decrypt(c, B):
    # lower b is used to encrypt
    global a
    global p
    global g
    kinverse = (B ** (p-a-1)) % p
    m = (c*kinverse) % p
    print("K-1:", kinverse)
    print("m:", m)


if __name__ == '__main__':
    print("Executing...")
    B = 4
    c = 19
    decrypt(c, B)
    print("Complete")
