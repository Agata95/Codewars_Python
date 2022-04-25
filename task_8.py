# Roman Numerals Decoder
# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
# You don't need to validate the form of the Roman numeral.
#
# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
# starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC)
# and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in
# descending order.
#
# Example:
# solution('XXI') # should return 21

def solution(roman):
    translate = [{'rom': 'I', 'int': 1},
                 {'rom': 'V', 'int': 5},
                 {'rom': 'X', 'int': 10},
                 {'rom': 'L', 'int': 50},
                 {'rom': 'C', 'int': 100},
                 {'rom': 'D', 'int': 500},
                 {'rom': 'M', 'int': 1000}]
    result = 0
    tab = []
    for i in range(0, len(roman)):
        tab.append(roman[i])
        for t in translate:
            if tab[i] == t['rom']:
                tab[i] = t['int']
    for i in range(0, len(tab)-1):
        if i < len(tab):
            if tab[i] > tab[i + 1]:
                print(i)
                print(tab[i])
    return result


print(solution('XXI'))
# print(solution('I'))
# print(solution('IV'))
# print(solution('MMVIII'))
# print(solution('MDCLXVI'))
# print(solution('MCMXC'))
