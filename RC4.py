import random
import string

def encrypt(plain, key):

    plain = [ord(c) for c in plain]

    return "".join(convert_list(plain, key))

def decrypt(cipher, key):

    cipher = [int(cipher[i:i+2], 16) for i in range(0, len(cipher), 2)]

    return "".join(chr(int(c, 16)) for c in convert_list(cipher, key))

def convert_list(l, k):

    length = len(l)

    stream = generate_keystream(k, length)

    return [hex(l[i] ^ stream[i])[2:].zfill(2) for i in range(length)]

def generate_keystream(key, length):

    key = [ord(c) for c in key]

    array = key_schedule(key)

    return generate_psuedorandom_numbers(array, length)

def key_schedule(key):

    length = len(key)

    array = list(range(256))

    j = 0

    for i in range(256):

        j = (j + array[i] + key[i % length]) % 256
        temp = array[j]
        array[j] = array[i]
        array[i] = temp
    
    return array

def generate_psuedorandom_numbers(array, length):

    i = 0
    j = 0

    numbers = []

    while length > 0:

        i = (i + 1) % 256
        j = (j + array[i]) % 256
        temp = array[j]
        array[j] = array[i]
        array[i] = temp

        numbers.append(array[(array[i] + array[j]) % 256])

        length -= 1
    
    return numbers

p = "Computer Science"
k = "AQACS"
e = encrypt(p, k)
print(p, "->", e, "->", decrypt(e, k))

if __name__ == "__main__":

    #unit tests

    test_no = 1
    test_length = 10
    alphabet = str(filter(lambda c: c not in string.whitespace, string.printable)) + " "

    random.seed(1000)

    for x in range(test_no):

        p = "".join(random.choice(alphabet) for _ in range(test_length))
        k = "".join(random.choice(alphabet) for _ in range(random.randrange(3, 10)))
        e = encrypt(p, k)
        d = decrypt(e, k)
        print(p, "->", e, "->", d, end="")
        if d != p:
            print(" (FAILED)")
            break
        else:
            print(" (PASSED)")