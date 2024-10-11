calls = 0
def count_calls():
         global calls
         calls +=1
         return(calls)
    
def string_info(string:str):
    count_calls()
    x = []
    x1 = string.upper()
    x2 = string.lower()
    x3 = (len(string))
    x3 = str(x3)
    x.append(x1)
    x.append(x2)
    x.append(x3)
    x = tuple(x)
   
    print(1,calls)
    return(x)
     
def is_contains(string:str,list_to_search:list):
        count_calls()
        if string in list_to_search:
            return(True)
        else:
            return(False)
    


    
            
            
   


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
