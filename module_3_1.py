calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    count_calls()
    tuple_for_str = (len(string), string.upper(), string.lower())
    return tuple_for_str


def is_contains(string, my_list):
    count_calls()
    string = string.lower()
    for i in my_list:
        i = str(i)
        i = i.lower()

    if string in my_list:
        return True
    else:
        return False


print(string_info("Urban"))
print(string_info("I am Pavel"))
print(is_contains("Python", [1, "python", "uRban", 86, 5.5]))
print(is_contains("Python", [10, "Dog", "X", 8.6, 513]))
print(calls)
