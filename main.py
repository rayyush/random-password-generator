import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"
length_password = int(input("Enter the length of the password required: "))
a = "".join(random.sample(password, length_password))

print(f"Your password is {a}")