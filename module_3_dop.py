data_structure = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
{'a': 4, 'b': 5, 'x': 10},
(6, {'cube': 7, 'drum': 8}),
"Hello", "Pavel",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum_args(*args):
    sum_ = 0
    for i in args:
        if isinstance(i, (int, float)):
            sum_ += i

        elif isinstance(i, str):
            sum_ += len(i)

        elif isinstance(i, (tuple, list, set)):
            sum_ += sum_args(*i)

        elif isinstance(i, dict):
            sum_ += sum_args(*i.items())

    return sum_


print(sum_args(*data_structure))
