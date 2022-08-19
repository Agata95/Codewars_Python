# Binary system
# Let us take a string composed of decimal digits: "10111213". We want to code this string as a string of 0 and 1 and after that be able to decode it.

decoder_bin = {
    '0': '10',
    '1': '11',
    '2': '0110',
    '3': '0111',
    '4': '001100',
    '5': '001101',
    '6': '001110',
    '7': '001111',
    '8': '00011000',
    '9': '00011001'
}

decoder_dz = {
    '10': '0',
    '11': '1',
    '0110': '2',
    '0111': '3',
    '001100': '4',
    '001101': '5',
    '001110': '6',
    '001111': '7',
    '00011000': '8',
    '00011001': '9'
}


def code(strng):
    strng_list = [int(a) for a in str(strng)]
    return ''.join([decoder_bin[str(el)] for el in strng_list])


def decode(strng):
    print(strng)
    strng = str(strng)
    text = []
    index = 0
    while len(strng) > 0:
        if not strng.startswith('0'):
            text.append(strng[index:index + 2])
            strng = strng[index + 2:]
        elif strng.startswith('01'):
            text.append(strng[index:index + 4])
            strng = strng[index + 4:]
        elif strng.startswith('001'):
            text.append(strng[index:index + 6])
            strng = strng[index + 6:]
        elif strng.startswith('0001'):
            text.append(strng[index:index + 8])
            strng = strng[index + 8:]

    return ''.join([decoder_dz[str(el)] for el in text])


# print(code('55337700'))
print(decode('001100001100001100001110001110001110011101110111001110001110001110001111001111001111001100001100001100'))
