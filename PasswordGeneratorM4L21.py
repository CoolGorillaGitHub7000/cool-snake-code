import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

password = ""
password += random.choice(characters)
for chars in range(8):
    print(password)