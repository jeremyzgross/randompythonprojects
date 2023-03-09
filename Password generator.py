# password generator practice

import random


chars = r"!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';"

while 1:
    password_len = int(input("What length would you like your password to be?:"))
    password_count = int(input("How many passwords would you like to generate?:"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("This is your password: ", password)
    exit()
