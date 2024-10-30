def get_multiplied_digits(numbers:int):
    str_number = str(numbers)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first



if __name__ == '__main__':
    print(get_multiplied_digits(219))