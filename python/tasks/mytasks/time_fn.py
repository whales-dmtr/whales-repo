import time


def time_fn(fun):
    """Дополнительно возвращает время действия функции"""
    def wrapper(*args, **kwargs):
        start = time.time()
        do_fun = fun(*args, **kwargs)
        end = time.time()
        fun_time = end - start

        # :.10f выводит число в десятичном виде
        print(f"Time of working function {fun_time:.10f}")
        return do_fun
    return wrapper
