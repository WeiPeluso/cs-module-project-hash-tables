# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {value: key for key, value in encode_table.items()}


def read_file():
    file = open("ciphertext.txt", "r")
    return file.read()


def decrypt(s):
    result = ''
    for c in s:
        if c.isalpha():
            result += decode_table[c]
        else:
            result += c
    return result


print("before:")
print(read_file())
print("after")
print(decrypt(read_file()))
