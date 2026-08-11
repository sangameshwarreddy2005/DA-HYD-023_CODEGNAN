'''
Ask the user to enter a sentence. Display
the same sentence in several different letter
cases.
Store the case-conversion method names in a
collection and use a loop to display each
result.
2. Display the text using upper(), lower(),
title(), capitalize(), swapcase()
3. Use conditions with isupper(), islower(), and
istitle() to describe the original text.
Example input: welcome to PYTHON
Upper : WELCOME TO PYTHON
Lower : welcome to python
Title : Welcome To Python
Capitalized : Welcome to python
Swap case : WELCOME TO python

user_text = input("Enter a sentence: ")
conversion_methods = [
    ("Upper", str.upper),
    ("Lower", str.lower),
    ("Title", str.title),
    ("Capitalized", str.capitalize),
    ("Swap case", str.swapcase),
    ("Casefold", str.casefold),
]
print("\n--- Converted Cases ---")
for label, method in conversion_methods:
    print(f"{label:<11} : {method(user_text)}")
print("\n--- Text Description ---")
if user_text.isupper():
    print("The original text is completely UPPERCASE.")
elif user_text.islower():
    print("The original text is completely lowercase.")
elif user_text.istitle():
    print("The original text is in Title Case.")
else:
    print("The original text contains a mix of uppercase and lowercase letters.")

'''

username = input("Enter username (or 'quit' to exit): ")
while True:
    if username.isidentifier():
        print("Valid Python identifier")
        break
    else:
        if username.isascii():
            print("Contains only ASCII characters")
            break
        else:
            if username[0].isalpha():
                print("Begins with a letter")
                break
    else:
        print("Does not begin with a letter")

    if username.isalnum():
        print("Contains only letters and numbers")
        break
    else:
        print("Does not contain only letters and numbers")

    print() 




















