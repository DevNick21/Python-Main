import time


def delay_func(func):
    def wrapper():
        time.sleep(2)
        func()
    return wrapper


@delay_func
def fuck():
    return "fucking..."


fuck()
