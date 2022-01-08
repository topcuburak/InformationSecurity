from Crypto.Cipher import AES   ##AES related libraries 
from Crypto.Util import Counter
import binascii
import os       

def encrypt_part_a(plaintext, key):     ## encryption function takes key and plaintext, and generates ciphertext
    aes = AES.new(key, AES.MODE_CTR, counter = Counter.new(128))
    ciptext = aes.encrypt(plaintext)
    return ciptext.hex()

def part_a(KEY_str):        ## part A that finds plaintext whose corresponding C[15] = 0x01
    KEY = binascii.hexlify(KEY_str.encode())    
    ptext = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    for i in range(0 , pow(2, 128)):   ## loops 2^128 amount
        res = encrypt_part_a(ptext, KEY)
        if res[30:32] == '01':  
            print("founded when i = " + str(i))
            break
        else:
            ptext = (i).to_bytes(16, 'big')
    print("KEY = " + str(KEY))
    print("Message for which C[15] = 0x01 is ---->" + str(binascii.hexlify(ptext)))
    print("\n")

def encrypt_part_b(plaintext, key):     ## encryption for part B
    aes = AES.new(key, AES.MODE_CTR, counter = Counter.new(128))
    ciptext = aes.encrypt(plaintext).hex()
    if ciptext[30:32] == '01':  ## if last byte of generated cipher text is 0x01
        return 1    ## return 1
    else:           ## other wise 0
        return 0

def part_b(plaintext):  ## part B which finds key that generates a ciphertext[15] = 0x01 for a constant plain text
    key = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    key_found = ""
    for i in range(0 , pow(2, 128)):    ## loops 2^128 amount
        res = encrypt_part_b(plaintext, key)
        if res == 1:
            print("founded when i = " + str(i))
            break
        else:
            key = (i).to_bytes(16, 'big')

    print("MESSAGE = " + str(plaintext))
    print("Key for which C[15] = 0x01 is ---->" + str(binascii.hexlify(key)))
    print("\n")

key_string = "This is the key!"
#key_string = input("please enter key of 16 characters used to find Message where C[15] = 0x01: ")
part_a(key_string)

plaintext_str = "ThisisThisisSSSS"
#plaintext_str = input("please enter plaintext of 16 characters used to find Key where C[15] = 0x01: ")
part_b(plaintext_str)
