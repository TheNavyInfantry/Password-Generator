import string
import random

def easy_password(length):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for x in range(length))
    return password

def medium_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for x in range(length))
    return password

def hard_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation + string.printable
    password = ''.join(random.choice(characters) for x in range(length))
    return password