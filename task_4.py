# Does my number look big in this?
# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number
# of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
#
# For example, take 153 (3 digits), which is narcisstic:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# 153 = 153

# and 1652 (4 digits), which isn't:
# 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# 1652 != 1938

def narcissistic(number):
    length = len(str(number))
    result = 0
    for i in str(number):
        result += pow(int(i), length)
    if result == number:
        return True
    else:
        return False

print(narcissistic(153))
print(narcissistic(1652))