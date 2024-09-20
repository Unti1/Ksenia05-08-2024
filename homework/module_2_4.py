"""Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
Цель: закрепить навык решения задач при помощи цикла for, применив знания об основных типах данных.

Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:
Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).

Пример результата выполнения программы:
Исходный код:
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Вывод на консоль:
Primes: [2, 3, 5, 7, 11, 13]
Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
Примечания:
Учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
Для проверки на простоту числа вам нужно убедиться, что выбранное число не делиться ни на что в диапазоне от 2 до этого числа(не включительно).
Попробуйте оптимизировать(ускорить) процесс выяснения простоты числа при помощи оператора break, когда найдёте делитель. (Не обязательно)
Переменные меняющее своё булевое состояние на противоположное в процессе проверки, как is_prime, в кругах разработчиков называются перменными-флагами(flag).
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# проход по значениям списка numbers
for num in numbers:
    if num != 1:
        d_lst = [] # список для делителей
        # проход по диапазону чисел(возможных делителей)
        for d in range(1, num+1):
            if num % d == 0:
                d_lst.append(d)
        
        print(f'Число {num} | Делители: {d_lst} | Количество делителей: {len(d_lst)}')
        if len(d_lst) == 2: # длина списка d_lst равна двум? Там 2 числа?
            primes.append(num) # если да то простое
        else: # иначе
            not_primes.append(num)

        


print('Primes: ', primes)
print('Not Primes: ', not_primes)