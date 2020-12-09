from time import sleep
from functools import lru_cache
import os
import random


# нормльно работает со строками, с интами плохо - это примитивный кэш
# можно использовать pickle тогда будет работать не со строками
# работает только для детерминированных функций
def cache(func):

    def wrapper(*args, **kwargs):
        # file_name = f'{"-".join(args)}-cache.txt'
        file_name = f'{"-".join([str(x) for x in args])}-cache.txt'

        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                return f.read()

        with open(file_name, 'w') as f:
            value = func(*args, **kwargs)
            f.write(str(value))
            return value

    return wrapper


@cache
# def long(a, b, c):
def long(a, b):
    sleep(5)
    # return a + b + c
    return random.randint(a, b)


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # a = [fib(x) for x in range(10000)]
    # print(a)
    print(long(0, 22))

