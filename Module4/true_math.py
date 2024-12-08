from math import inf

def divide(first, second):
    if second  == 0:
        res = float(inf)
    else:
        res = first / second
    return res

# print(divide(4, 0))