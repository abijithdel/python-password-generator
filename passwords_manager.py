import random
import string
def check(len,uppercase,lowercase,symbols,number):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if symbols:
        characters += string.punctuation
    if number:
        characters += string.digits
    if not characters:
        print('error')

    password = ''.join(random.choice(characters) for In in range(len))

    return password 
      
leng = int(input('Enter password Length: '))

pass_uppercase = input('Include Uppercase yes/no: ').lower() == 'yes'
pass_lowercase = input('Include Lowercase yes/no: ').lower() == 'yes'
pass_symbols = input('Include Symbols yes/no: ').lower() == 'yes'
pass_number = input('Include Number yes/no: ').lower() == 'yes'


password = check(leng,pass_uppercase,pass_lowercase,pass_symbols,pass_number)

print(password)