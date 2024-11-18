value_list = [15, "Pavel", [1, 22, 333]]
values_dict  = {"a":"Name", "b":88, "c":[2, 3, 4]}
value_list_2 = [86.55, "Pavel"]

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print()
print_params(*value_list)
print_params(**values_dict)
print_params(*value_list_2, 42)

