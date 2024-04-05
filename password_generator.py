import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    specials=string.punctuation

    characters=letters
    if numbers:
        characters+=digits
    if special_characters:
        characters+=specials
    
    pwd=""
    meets_criteria=False
    has_numbers=False
    has_specials=False

    while not meets_criteria or len(pwd)<min_length:
        new_character=random.choice(characters)
        pwd+=new_character

        if new_character in digits:
            has_numbers=True
        if new_character in specials:
            has_specials=True

        meets_criteria=True
        if numbers:
            meets_criteria=has_numbers
        if special_characters:
            meets_criteria=meets_criteria and has_specials
    
    return pwd

min_length=int(input("Enter the minimum length: "))
numbers=input("Do you want numbers (y/n): ").lower() == 'y'
special_characters=input("Do you want special characters (y/n): ").lower() == 'y'
print("Your generated password is",generate_password(min_length,numbers,special_characters))


