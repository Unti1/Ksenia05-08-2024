'''Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.

Задача:
Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями. К каждой библиотеке дана ссылка 
на документацию ниже.
Если вы выбрали:
requests - запросить данные с сайта и вывести их в консоль.
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека и как 
вы расширили возможности Python с её помощью.
Примечания:
Можете выбрать не более 3-х библиотек для изучения.
Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.
Файл module_11_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него и комментарий к использованным инструментам библиотек(-и).
Успехов!'''

import requests
def func():
    y=input('Привет! Чтобы узнато погоду, введи свой город!').strip()
    params = {'q':y,'appid':'9a835dd3e649f855b9a1c339d8237ad1','units':'metric'}
    
    response = requests.get('https://api.openweathermap.org/data/2.5/weather',params=params)
    x=response.json()
    result=x['main']['temp']
    print(f'Погода в {y}:{result}')   

def func1():
    params = {'q':'чихуаху'}
    response = requests.get('https://yandex.ru/search',params=params)
    print(response.json)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(np.mean(arr))
random_numbers = np.random.random(5)
print(random_numbers)
   
import pandas as pd 

df=pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')
print(type(df))


df1=pd.DataFrame.from_dict({'Name':['Ann','Ben','Dan'],'Age':[22,22,33]})

print(df['Name'],['Age'])

data = np.array([1, 2, 3, 4, 5])
df = pd.DataFrame(data, columns=["Values"])
print(df)

import matplotlib.pyplot as x

data = [1,2,3,4,5,6,7,8]
x.hist(data, bins=30, edgecolor='black')


x.title("Гистограмма случайных чисел")
x.xlabel("Значение")
x.ylabel("Частота")
x.savefig('/Users/ksenia/Downloads/Новая папка/gg')

from PIL import Image, ImageDraw, ImageFont

# Открытие изображения
image = Image.open('/Users/ksenia/Downloads/Новая папка/gg.png')

# Создание объекта для рисования
draw = ImageDraw.Draw(image)

# Выбор шрифта (можно указать путь к файлу шрифта)
font = ImageFont.truetype("/Library/Fonts/Arial.ttf", size=149)

# Добавление текста на изображение
draw.text((100, 100), "Привет, мир!", font=font, fill="pink")

# Сохранение изображения с текстом
image.save('/Users/ksenia/Downloads/Новая папка/gg.png')
