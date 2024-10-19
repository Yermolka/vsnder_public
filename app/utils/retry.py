from functools import wraps
from typing import Callable
from asyncio import sleep


def retry(max_retries = 3, timeout = 0.5):
    def wrapper(func: Callable):
        @wraps(func)
        async def wrap(*args, **kwargs):
            for i in range(max_retries):
                try:
                    await func(*args, **kwargs)
                except Exception as ex:
                    #logger.log(ex)
                    print(f"Func {func} exception: {ex}. Retry {i+1} of {max_retries}")
                    await sleep(timeout)
        
        return wrap

    return wrapper
