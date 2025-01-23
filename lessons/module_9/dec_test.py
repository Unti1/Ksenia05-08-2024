import time, sys

def func_gen_dec(precision: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end   = time.time()
            print(f"Время выполнения: {end - start:.{precision}f} секунд. Размер результата: {sys.getsizeof(result)}")
            return result
        return wrapper
    return decorator

sys.set_int_max_str_digits(10**5)

@func_gen_dec(2)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 500
    return(len(str(total)))

result = digits(*[i for i in range(10)])
print(result)


# time_track_percision_6 = func_gen_dec(6)
# digits = time_track_percision_6(digits)
# result = digits(*[i for i in range(100000)])
# print(result)

# @time_track_percision_6
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 500
#     return(len(str(total)))

# result = digits(*[i for i in range(100000)])
# print(result)
