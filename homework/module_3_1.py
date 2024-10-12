calls = 0

def string_info(string:str):
    global calls
    calls +=1 
    x = []
    x1 = string.upper()
    x2 = string.lower()
    x3 = len(string)
    x3 = str(x3)
    x.append(x1)
    x.append(x2)
    x.append(x3)
    x = tuple(x)
    return(x)
    
def is_contains(string:str,list_to_search:list):
        global calls
        calls +=1 
        if string in list_to_search:
            return(True)
        else:
            return(False)
            
def count_calls():
    print(calls)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Armageddon'))
print(is_contains('ban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)