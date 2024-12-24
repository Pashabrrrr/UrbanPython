import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # читаем файл и обрабатываем строки
                    text = file.read().lower()
                    # убираем пунктуацию
                    text = text.translate(str.maketrans('', '', string.punctuation))
                    # разбиваем строку на слова
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f'Файл {file_name} не найден.')

        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1
                result[file_name] = position

        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count

        return result

# Пример выполнения программы

finder = WordsFinder('test_file.txt')

print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')

print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))