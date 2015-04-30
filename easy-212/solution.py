from itertools import chain
from string import ascii_lowercase

consonants = set(ascii_lowercase) - set('aeiouy')


def addos(x):
    return [x, 'o', x.lower()] if x.lower() in consonants else [x]


def encode(msg):
    return ''.join(chain.from_iterable(map(addos, msg)))


def decode(msg):
    out = []
    i = 0
    while i < len(msg):
        x = msg[i]
        out.append(x)
        if x.lower() in consonants:
            i += 2
        i += 1

    return ''.join(out)
