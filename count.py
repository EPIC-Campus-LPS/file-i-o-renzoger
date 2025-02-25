import string 

def count(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    
    amount = {letter: text.count(letter) for letter in string.ascii_lowercase if letter in text}
    
    for letter, count in sorted(amount.items()):
        print(f"{letter}: {count}")

file = input("file: ")
count(file)
