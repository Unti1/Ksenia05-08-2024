list1 = [12, 45, 89, 66]
list = ("HI", "DFDGDH", 'dhdggd')
list1.append("Привет")
print(list1)
list1.insert(0, 3)
print(list1)
print(list)
list1.extend(list)
print(list1, type(list1)) # Если мы вставляем в список кортеж, то он становится списком 
print(list)
print(list1)
"""list.extend(list1)
print(list, type(list)) В картеж нельзя добавить список, а в список можно""" 
list = [12, 45, 89, 66]

list1.remove(12)
print(list1)
list.pop(0)
print(list)
fdfg = list.pop(0)
print(fdfg)
