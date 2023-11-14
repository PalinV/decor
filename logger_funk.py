from datetime import datetime
from functools import wraps


def __logger(path):
    def logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            start = str(datetime.now())
            result = old_function(*args, **kwargs)
            with open(path, mode='a', encoding='UTF8') as log:
                log.write(f'Функция {old_function.__name__} была вызвана {start} с аргументами {args} и {kwargs}. Получен результат: {result}\n')
            return result
        return new_function
    return logger


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = str(datetime.now())
        result = old_function(*args, **kwargs)
        with open('main.log', mode='a', encoding='UTF8') as log:
            log.write(f'Функция {old_function.__name__} была вызвана {start} с аргументами {args} и {kwargs}. Получен результат: {result}\n')
        return result
    return new_function