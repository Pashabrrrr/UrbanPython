def single_root_words(root_word: str, *other_words):
    same_words: list = []
    rw = root_word.lower()
    for word in other_words:
        w = word.lower()
        if w in rw or rw in w:
            same_words.append(word)
    return same_words


res1 = single_root_words("Макс", "максимум", "максимальный", "Бимакс", "Питон", "БигМак")
print(res1)

res2 = single_root_words("многоугольник", "УГОЛ", "Угольник", "гол", "машина", "Питон")
print(res2)



