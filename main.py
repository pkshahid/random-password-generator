import random
import string
LETTERS = string.ascii_letters
NUMS = "0123456789"
SPC = "-+*&%$#@!_"
SYMBOLS = f"{LETTERS}{SPC}{NUMS}"
len = int(input("Enter Length Of Password:"))
password=''.join(random.sample(SYMBOLS,len))
print("The password is : ",password)
