import random


print("="*20)
print("Password Generator")
print("="*20)
length = int(input("How many character you want: "))
password = "" 



letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
special_character = "@!%$#&*"

random_character = [letter, digit, special_character]

for i in range(0, length):
    character = random.choice(random_character)
    password += random.choice(character)

print("Your password:", password)

