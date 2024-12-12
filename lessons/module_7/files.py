
name = 'lessons/module_7/text.txt'
# file = open(name, 'r')
# print(file.read())
# file.close()
# print(file.read())

with open(name, 'r') as file:
    print(f'{file.read()=}')

# print(file.read())

name = 'lessons/module_7/text1.txt'
with open(name, 'w') as file:
    print(file.write('\nhello\nworld'))
    # print(file.read())

with open(name, 'a') as file:
    print(file.write('\nhello world2'))



with open(name, 'rb') as file:
    print(file.read())


with open(name, 'ab') as file:
    print(file.write('tell'.encode()))