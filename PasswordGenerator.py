import random
length = int(input("Enter Length of Password: ")) 
symbol = '!@#$%^&*()'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
password = ''
i = 0
while i <= length:
    num = random.randint(0,9)
    password += alphabet[num]
    password += symbol[num]
    password += str(num)

    i += 1
    
print(password[:10])