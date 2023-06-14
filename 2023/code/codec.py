
SYMBOLS = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y',
    'Z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x',
    'y', 'z', ' ']


def encode(input):
    encoded = []
    for w in input:
        invalid_sym = True
        for i in range(len(SYMBOLS)):
            if w == SYMBOLS[i]:
                invalid_sym = False
                encoded.append(i)
        if invalid_sym:
            raise ValueError("invalid symbol")
    enc = "".join(str(x).zfill(2) for x in encoded)
    return enc

def decode(encoded):
    numbs = []
    for i in range(0, len(encoded), 2):
        num = f"{encoded[i]}{encoded[i + 1]}"
        numbs.append(SYMBOLS[int(num)])
    return "".join(numbs)
words = input("Masukan: ")
enc = encode(words)
print(enc)
print(decode(enc))