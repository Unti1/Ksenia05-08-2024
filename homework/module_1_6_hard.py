grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

spisok = {} 

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
print(b3, type(b3))

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

student1 = list(students)


aa1 = student1.pop()
print(aa1, type(aa1))
bb1 = student1.pop()
cc1 = student1.pop()
dd1 = student1.pop()
ff1 = student1.pop()

x = [[aa1,a3],[bb1,b3], [cc1,c3], [dd1,d3],[ff1,f3]]
itog = dict(x)
dd = dict(sorted(itog.items()))
print(F'Ответ задачи: {dd}')





















