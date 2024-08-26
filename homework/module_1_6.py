my_dict = {
'Name':['Ksusha'],
'Age':[22] }
print(my_dict)

print(f'HER NAME IS {my_dict.get('Name')}')
print(my_dict.get('mdm', 'Not found'))
my_dict.setdefault('Country', ['Russia'])
my_dict.setdefault('Marital status', ['Single']) # Вопрос: зачем в значении ставить скобки, если можно без них ? 
print(my_dict)

a = my_dict.pop('Age')
print(a)
print(my_dict)

my_set0 = {10,10,'10','Hi', 22,23}
my_set = set(my_set0)
print(my_set)
my_set.add('hdd')
my_set.add(33)
print(my_set)
my_set.remove(10)
print(my_set)



