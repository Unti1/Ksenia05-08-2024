'''Домашнее задание по теме "Оператор "with".
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.

Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count

Пример результата выполнения программы:
Представим, что файл 'test_file.txt' содержит следующий текст:


Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

Вывод на консоль:
{'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
{'test_file.txt': 3}
{'test_file.txt': 4}

Запустите этот код с другими примерами предложенными здесь.
Если решение верное, то результаты должны совпадать с предложенными.

Примечания:
Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
Решайте задачу последовательно - написав один метод, проверьте результаты его работы.

Файл module_7_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!'''
import os
class WordsFinder:
    def __init__(self,*file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        all_words = {}
        for x in self.file_names:
            with open(x,'r',encoding='utf-8') as file:
                y = file.read().lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    y1= y.replace(char, ' ')
                    y2 = y1.split()
                    all_words[x] = y2
        return all_words
    def find(self, word):
        z ={}
        x= self.get_all_words()
        word=word.lower()
        for file_name,words in x.items():
            if word in words:
                z[file_name]=words.index(word)
            else:
                z[file_name]= None
        return z        
    def count(self, word):
        z1 ={}
        word=word.lower()
        x= self.get_all_words()
        for file_name,words in x.items():
                z1[file_name]=words.count(word)  
        return z1      






                



a = WordsFinder('homework/file1.txt', 'homework/file2.txt')
print(a.get_all_words())
print(a.find('gHgh'))
print(a.count('gHgh'))