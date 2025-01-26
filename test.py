class Iter:
    def __init__(self):
        self.first = 'Первый элемент'
        self.second = 'Второй элемент'
        self.third = 'Третий элемент'
        self.i = 0
    
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        self.i += 1
        match self.i: # if self.i ==
            case 1: # == 1
                return self.first
            case 2: #elif self.i == 2
                return self.second
            case 3: #elif self.i == 3
                return self.third
            case 4: #elif self.i == 4
                return "Подсчёт заного"
            case _: # else
                raise StopIteration()

it = Iter()

print(it)
print(list(it))

for value in it:
    print(value)

