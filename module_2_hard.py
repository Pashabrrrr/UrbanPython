# Слишком древний шифр

n = int(input("Введите число от 3 до 20: "))
if n < 3 or n > 20:
    print("Первый раз прощается, второй запрещается")
    n = int(input("Еще раз попробуйте: "))


def password_selection(n):
    if n < 3 or n > 20:
        x = ("Вас предупреждали! От шипов никому не уйти!")
        return x
    else:
        pass_ = str("")
        for i in range(1, 21):
            if i != n:
                for j in range(1, 21):
                    if j != n and j > i and n % (i + j) == 0:
                        pass_ = pass_ + str(i) + str(j)
                    else:
                        continue
            else:
                continue
        return pass_


result = password_selection(n)
print(result)
