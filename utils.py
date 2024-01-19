from time import time
import inspect


def timeit(func):
    async def wrapper_async(*args, **kwargs):
        t1 = time()
        await func(*args, **kwargs)
        t2 = time()
        print(f'Função assíncrona {func.__name__} executou em {t2 - t1} segundos')

    def wrapper_sync(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'Função síncrona {func.__name__} executou em {t2 - t1} segundos')

    if inspect.iscoroutinefunction(func):
        return wrapper_async
    else:
        return wrapper_sync