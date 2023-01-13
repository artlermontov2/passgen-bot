import random


def password(list_characters: list[str]) -> str:
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    for i in list_characters:
        # uppercase
        if 'up' in i:
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        # special
        if 'spec' in i:
            characters.extend(list('!@#$%&*()-_+=;:,./?\~'))
        # numbers
        if 'num' in i:
            characters.extend(list('1234567890'))
    
    the_pass = ''

    try:
        length = int(list_characters.pop())
        for _ in range(length):
            the_pass += random.choice(characters)

    except ValueError:    
        length = 8
        for _ in range(length):
            the_pass += random.choice(characters)

    return the_pass


def pars_msg(text: str) -> list[str]:
    message = text.lower().split(' ')
    return message

print(pars_msg('Num 9'))