import string

def ceasar_cypher_encode(data:str, n: int) -> str:
    from_letters = 'abcdefghijklmnopqrstxyz'
    if n >= 0:
        to_letters = from_letters[n:] + from_letters[:n]
    else:
        n = abs(n)
        to_letters = from_letters[-n:] + from_letters[:-n]
    return data.translate(str.maketrans(from_letters, to_letters))

def ceasar_cypher_decode(data:str, n: int) -> str:
    from_letters = 'abcdefghijklmnopqrstxyz'
    if n >= 0:
        to_letters = from_letters[n:] + from_letters[:n]
    else:
        n = abs(n)
        to_letters = from_letters[-n:] + from_letters[:-n]
    return data.translate(str.maketrans(to_letters, from_letters, ))

my_str = "hello, world"

chyphed = ceasar_cypher_encode(my_str, 4)
decyphed = ceasar_cypher_decode(chyphed, 4)

# print(ceasar_cypher_encode())

print(chyphed)
print(decyphed)

print(string.ascii_lowercase)