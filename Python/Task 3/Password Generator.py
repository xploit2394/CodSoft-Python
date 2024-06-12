import random
import string

def password_generator():
    length = int(input("Enter the desired length of the password: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    print("Generated Password : ", password)

password_generator()