import string
import random

length = int(input("Password length: "))

charList = string.digits + string.ascii_letters + string.punctuation

passwd = []

for i in range(length):
    randChar = random.choice(charList)
    passwd.append(randChar)

print("Generated password: " + "".join(passwd))
