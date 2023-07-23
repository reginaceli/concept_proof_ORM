from random import sample,shuffle
from string import ascii_letters,digits,punctuation

def generate_password(size=8):
    """\
    Random password generator, and its length is defined by adm-user
    Default this app = 8
    """

    password = sample(ascii_letters+punctuation+digits, size)

    shuffle(password)

    return(''.join(password))
