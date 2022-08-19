# RGB To Hex Conversion
# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.

def rgb(r, g, b):
    if r > 255:
        r = 255
    elif r < 0:
        r = 0
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    if b > 255:
        b = 255
    elif b < 0:
        b = 0

    dictionary = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"}

    tab = []
    for n in [r, g, b]:
        number = n
        tab2 = []
        if number >= 16:
            while number >= 16:
                modulo = number % 16
                tab2.append(modulo)

                number = int(number / 16)
                if number < 16:
                    tab2.append(number)
        else:
            tab2.append(number)
        tab2.reverse()

        for x in range(0, len(tab2)):
            if tab2[x] >= 10:
                for k, v in dictionary.items():
                    if tab2[x] == k:
                        tab2[x] = v
            elif len(tab2) == 1:
                tab2[x] = '0' + str(tab2[x])
            else:
                tab2[x] = str(tab2[x])

        tab += tab2

        print(tab)

    return ''.join(tab)


# print(rgb(0, 0, 0))
# print(rgb(1, 2, 3))
# print(rgb(254, 255, 255))
# print(rgb(-20, 275, 125))
print(rgb(275, -20, 125))
