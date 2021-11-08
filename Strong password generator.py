from random import sample

length = int(input("Please enter the desired password length: "))
lencheck = length >= 5
if lencheck == False:
    print("Password length must be at least 5 characters!")
else:
    c1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c2 = "abcdefghijklmnopqrstuvwxyz"
    c3 = "1234567890"
    c4 = "!@#$%&*?"
    c5 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    step1 = "".join(sample(c1, 1))
    step2 = "".join(sample(c2, 1))
    step3 = "".join(sample(c3, 1))
    step4 = "".join(sample(c4, 1))
    step5 = "".join(sample(c5, length-4))
    string = step1+step2+step3+step4+step5
    password = "".join(sample(string, length))
    print(password)
