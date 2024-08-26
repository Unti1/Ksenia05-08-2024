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

slovar1 = {
    "Анна":[18],
    "Ксения":[26],
    "Елена":[33] 
    }

ddg = [10,11.12]
print(ddg[0])

hch = [20,'ghgh']
hch.append('dhdh')
print(f"YI {hch}")

print(f'dgdg {hch.insert(0,20)}')
print(hch)


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

d = grades.pop(4)
d1 = sum(d)
d2 = len(d)
d3 = (d1/d2)
print(d)

print(grades.index([5, 5, 5, 4, 5]))

a = grades.pop(0)
a1 = sum(a)
a2 = len(a)
a3 = (a1/a2)
print(a3)

b = grades.pop(0)
b1 = sum(b)
b2 = len(b)
b3 = (b1/b2)
print(b3)

c = grades.pop(0)
c1 = sum(c)
c2 = len(c)
c3 = (c1/c2)
print(c3)

d = grades.pop(0)
d1 = sum(d)
d2 = len(d)
d3 = (d1/d2)
print(d3)

f = grades.pop(0)
f1 = sum(f)
f2 = len(f)
f3 = (f1/f2)
print(f3)

aa1 = student11.pop()
print(aa1, type(aa1))
bb1 = student11.pop()
cc1 = student11.pop()
dd1 = student11.pop()
ff1 = student11.pop()

x = [[aa1,a3],[bb1,b3], [cc1,c3], [dd1,d3],[ff1,f3]]
itog = dict(x)
print(itog)
