import random
import string

def generate_password(length):
    

    if length < 8:
        return None

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lowercase),       
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols,
    background="#5933DF",

    for _ in range(length - 8):password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)
    