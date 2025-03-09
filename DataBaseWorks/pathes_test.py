import os


print(f'{__file__=} {type(__file__)}')
# print(globals())
abs_path = os.path.abspath(__file__)
print(f'{abs_path=} {type(abs_path)}') # перестраховка для корректного вывода пути к файлу
print(f'{os.path.dirname(os.path.abspath(__file__))=}')



