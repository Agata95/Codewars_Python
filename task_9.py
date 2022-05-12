# Valid Parentheses
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
import re


def valid_parentheses(string):
    tab = []

    for x in string:
        if x in ["(", ")"]:
            tab.append(x)

    total = []
    print(tab)
    if len(tab) == 0:
        return True
    elif len(tab) % 2 == 0:
        for i in range(0, len(tab)):
            if (tab[0] == ')') or (tab[-1] == '('):
                return False
            else:
                if tab[i] == '(':
                    total.append(tab[i])
                else:
                    try:
                        total.remove('(')
                    except:
                        return False
        if len(total) == 0:
            return True
        else:
            return False
    else:
        return False


# print(valid_parentheses(")test)"))
# print(valid_parentheses("  ("))
# print(valid_parentheses(")test"))
# print(valid_parentheses(""))
# print(valid_parentheses("hi())("))
# print(valid_parentheses("hi(hi)()"))
# print(valid_parentheses("())(()"))
print(valid_parentheses("(hdyiwjxvcbp(yt(ivrouxbqmruv)kdfpzcbdwxu"))
