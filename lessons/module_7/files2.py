
name = 'lessons/module_7/text3.txt'

# with open(name, 'r', encoding='utf-8') as fl:
#     print(fl.tell())
#     text = str(fl.read(6))
#     print(text)
#     print(len(text))
#     print(fl.tell())

#     fl.seek(18)

#     #Прочитаем ещё раз
#     print(fl.tell())
#     text = str(fl.read())
#     print(text)
#     print(len(text))
#     print(fl.tell())

with open(name, 'w') as fl:
    print(fl.tell())
    # text = str(fl.write('Hello'))# Записывает нормально
    text = str(fl.write('Привет'))# Записывает как торабарщину
    print(fl.tell())


with open(name, 'wb') as fl:
    print(fl.tell())
    # text = str(fl.write('Hello'))
    text = str(fl.write('Привет'.encode()))
    print(fl.tell())