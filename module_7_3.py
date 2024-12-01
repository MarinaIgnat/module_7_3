import string

#Название класса
class WordsFinder:
#Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в
# атрибут file_names в виде списка или кортежа.
    def __init__(self, *file_names):
        self.file_names = file_names

#подготовительный метод,
    def get_all_words(self, *file_names):
        #Создайте пустой словарь
        all_words = {}
        #Переберите названия файлов и открывайте каждый из них
        for name in file_names:
            with open(file_names, encoding='utf-8') as file:
                #Для каждого файла считывайте единые строки, переводя их в нижний регистр
                lines = file.readline().lower()
                #Избавьтесь от пунктуации в строке
                for punctuation in string.punctuation:
                    if punctuation in lines:
                        lines = file.replace(punctuation, '')
                #Разбейте эту строку на элементы списка
                list_ = lines.split()
            all_words[name] = list_
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word)
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = len(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



