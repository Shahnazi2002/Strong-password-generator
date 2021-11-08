from random import sample

length = int(input("Please enter the desired password length: "))
character = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*?"
password = "".join(sample(character, length))
print(password)