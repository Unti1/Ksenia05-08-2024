####################################
# import test_module
# import main
# print(test_module.addition(2, 5))


###################################
# from test_module import addition, multiply

# print(addition(2,7))
# print(globals())


####################################
# import test_module as TM

# print(TM.addition(2,5))
# print(TM.multiply(2,5))
# print(globals())

####################################
from test_module import *
print(globals())
# print(addition(2,7))
# print(multiply(2,7))
# print(globals())