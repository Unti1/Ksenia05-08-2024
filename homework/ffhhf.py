v = 99
def x():
    global v
    print(87,v)
    v = 0
    print(33,v)
    def b():
        
        v = 8
        print(2,v)
        def m():
            nonlocal v
            print(6,v)
            v = v+9
            print(1,v)
        m()
        print(877,v)    
    b()
    print(5,v)
        
      
print(44,v)
print(x())
print(v)


