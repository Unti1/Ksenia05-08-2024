def func12(k:list):
    d = []
    l = []

    for i in k:
        d = len(i)
        l.append(d)
        j = dict(zip(k, l))
        
    return j    
        
print('26:',func12(['ssss','ddd','dddd']))   