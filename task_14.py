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
    return 0


# print(code(10111213))
print(decode(10111213))



