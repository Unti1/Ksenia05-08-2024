def print_params(a = 1, b = 'строка', c = True):
    return a,b,c

print(print_params(b = 25))    
print(print_params(c = [1,2,3]))


values_list = [1,'ff',{"key":10}]
values_dict = {"a":10,"b":'H','c':[1,2]}

print(print_params(values_list))    
print(print_params(values_dict))
print(print_params(*values_list))    
print(print_params(**values_dict))

values_list_2 = [11,'hi']

print(print_params(values_list_2, 42))
print(print_params(*values_list_2, 42))