# Завдання 1. Створити функцію, яка обчислює факторіал числа.
# Запустити декілька задач з використанням TreadPoolExecutor та
# ProcessPoolExecutor і виміряти швидкість обчислень в обох випадках.
# Додати до коду програму, який порівнює швидкість обчислень і виводить на друк
# найоптимальніший метод.

import concurrent.futures
import time


NUMBERS = [5, 10, 15, 20, 991]


# Створюю метод для обчислення факторіалу.
def factorial(x):
    if x < 2:
        return 1
    else:
        return x * factorial(x - 1)


# Створюю ProcessPoolExecutor для обчислення факторіалу.
def process():
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        for number, result in zip(NUMBERS, executor.map(factorial, NUMBERS)):
            print("%d is factorial: %s" % (number, result))


# Створюю ThreadPoolExecutor для обчислення факторіалу.
def thread():
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        for number, result in zip(NUMBERS, executor.map(factorial, NUMBERS)):
            print("%d is factorial: %s" % (number, result))


# Функція для порівння швидкості обчислень.
def compare():
    if duration_1 < duration_2:
        print('ProcessPoolExecutor is faster!')
        print('Process was executed within', duration_1)
    else:
        print('ThreadPoolExecutor is faster!')
        print('Process was executed within', duration_2)


# Запускаю програму.
if __name__ == '__main__':
    # ProcessPoolExecutor
    print('--- Task 1 ---')
    print("Calculating of factorial with ProcessPoolExecutor: ")
    start_time = time.time()
    process()
    duration_1 = time.time() - start_time
    print(f"Duration of execute = {duration_1}")
    print("=====" * 10)

    # ThreadPoolExecutor
    print("Calculating of factorial with ThreadPoolExecutor: ")
    start_time = time.time()
    thread()
    duration_2 = time.time() - start_time
    print(f"Duration of execute = {duration_2}")

    # Викликає функцію порівння.
    print("-----" * 10)
    print('What is faster: ProcessPoolExecutor vs ThreadPoolExecutor?')
    compare()
