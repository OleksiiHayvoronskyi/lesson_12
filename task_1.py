# Завдання 1. Створити функцію, яка обчислює факторіал числа.
# Запустити декілька задач з використанням TreadPoolExecutor та
# ProcessPoolExecutor і виміряти швидкість обчислень в обох випадках.
# Додати до коду програму, який порівнює швидкість обчислень і виводить на друк
# найоптимальніший метод.

import concurrent.futures
import time


# Числа для обчисленя факторіалу.
NUMBERS = [5, 10, 15, 20, 991]


# Створюю метод для обчислення факторіалу.
def factorial(x):
    if x < 2:
        return 1
    else:
        return x * factorial(x - 1)


# Створюю ProcessPoolExecutor для обчислення факторіалу.
def get_process():                        # кількість потоків (max_workers=10)
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for number, result in zip(NUMBERS, executor.map(factorial, NUMBERS)):
            print("%d is factorial: %s" % (number, result))


# Створюю ThreadPoolExecutor для обчислення факторіалу.
def get_thread():                         # кількість потоків (max_workers=10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for number, result in zip(NUMBERS, executor.map(factorial, NUMBERS)):
            print("%d is factorial: %s" % (number, result))


# Функція для порівння швидкості обчислень.
def get_compare():
    if duration_1 < duration_2:
        print('ProcessPoolExecutor is faster!')
        print('The process was executed in', duration_1, 'sec.')
    else:
        print('ThreadPoolExecutor is faster!')
        print('The process was executed in', duration_2, 'sec.')


# Запускаю програму.
if __name__ == '__main__':
    # ProcessPoolExecutor
    print('--- Task 1 ---')
    print("Calculating of factorial with ProcessPoolExecutor: ")
    start_time = time.time()
    get_process()
    duration_1 = time.time() - start_time
    print(f"Duration of execute = {duration_1} sec.")
    print("=====" * 10)

    # ThreadPoolExecutor
    print("Calculating of factorial with ThreadPoolExecutor: ")
    start_time = time.time()
    get_thread()
    duration_2 = time.time() - start_time
    print(f"Duration of execute = {duration_2} sec.")

    # Викликає функцію порівння.
    print("-----" * 10)
    print('What is faster: ProcessPoolExecutor vs ThreadPoolExecutor?')
    get_compare()
