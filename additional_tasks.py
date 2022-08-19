# 1. Find and return the missing number in a sequencial list
import copy
from timeit import default_timer


def find_missing_numbers(numbers):
    sort = sorted(numbers)
    return [x for x in range(sort[0], sort[-1] + 1)
            if x not in numbers]


numbers = [1, 2, 5, 4, 7, 11, 8, 9, 10]
print(find_missing_numbers(numbers))
print("----------------------------------------------------------------")


# 2. Reverse list
def reverse_list(lst):
    lst.reverse()
    return lst


lst = [0, 1, 2, 3, 4, 5]
print(reverse_list(lst))
print("----------------------------------------------------------------")


# 3. Sorted list
def sort_list(lst2):
    return sorted(lst2)


lst2 = [0, 4, 3, -1, 6, -3]
print(sort_list(lst2))
print("----------------------------------------------------------------")


# 4. Reverse key and values in dict
def reverse_key_value(dict):
    new_dict = {}
    for k, v in dict.items():
        new_dict[v] = k
    return new_dict


my_dict = {2: "black", 5: "blue", 8: "white"}
print(reverse_key_value(my_dict))
print("----------------------------------------------------------------")


# 5. Simple decorator
def decorator(func):
    def wrapper():
        print("Zaraz sie wykona")
        func()
        print("Done")

    return wrapper


@decorator
def hello():
    print("Hello World!")


hello()
print("----------------------------------------------------------------")


# 6. Decorator for measure time (return: result, start time, end time, measure time)
def measure_time(func):
    def inner(*args):
        t_start = default_timer()
        result = func(*args)
        t_end = default_timer()
        t = t_end - t_start
        return result, t_start, t_end, t

    return inner


@measure_time
def fibbonaci(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a


print("Result: ", fibbonaci(5))
print("----------------------------------------------------------------")

# 7. Iterator wbudowany
lst3 = [1, 3, 4]
iterator_listowy = iter(lst3)

print(iterator_listowy)
# pierwszy element listy:
print(next(iterator_listowy))
# i kolejne elementy listy:
print(next(iterator_listowy))
print(next(iterator_listowy))
print("----------------------------------------------------------------")


# 8. Zbudowanie własnego iteratora
class MyIterator():
    def __init__(self):
        self.x = 1
        self.max = 10

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x

        if x > self.max:
            raise StopIteration
        self.x += 3

        return x


for i in MyIterator():
    print(i)
print("----------------------------------------------------------------")


# 9. Zbudowanie iteratora odwracającego słowo
class Reverse():
    def __init__(self, data='Word'):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1
        return self.data[self.index]


for i in Reverse():
    print(i, end='')
print('')
print("----------------------------------------------------------------")


# 10. Generatory
def generator(a, b):
    while a <= b:
        yield a
        a += 2


for i in generator(4, 8):
    print(i)

print("----------------------------------------------------------------")


# 11. Generator reverse
def generator_reverse(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]


for i in generator_reverse([1, 2, 3, 4]):
    print(i)
print('')

for i in generator_reverse("kukulka"):
    print(i, end='')
print('')
print("----------------------------------------------------------------")

# 12. Copy and Deepcopy
# old_list = [1, 2, 3]
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
new_list[0][0] = 'c'

print("Id old list: ", id(old_list), " ", old_list)
print("Id new list: ", id(new_list), " ", new_list)
print("----------------------------------------------------------------")

# 13. Array - biblioteka numpy
import numpy as np

a = np.array([1, 2, 5, 6])
b = np.array([0, 5, 6, 7])
c = np.array([[1, 2, 3], [4, 5, 6]])

print(a+b)
print(a**2)
print(c)
print(c.T)
