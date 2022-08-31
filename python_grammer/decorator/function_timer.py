
import time

# value 까지의 피보나치 배열을 구하는 함수
def fibo(value):
    fibo_dict = dict()
    a, b = 0, 1
    for item in range(1, value+1):
        a, b, = b, a + b
        fibo_dict[item] = a
    return fibo_dict

# n! 을 구하는 함수
def factorial(n):
    i = n
    while i > 1:
        i -= 1
        n *= i
    return n

start = time.time()
print(fibo(50))
finish = time.time()
print(f"fibo execution: {finish-start}")


start2 = time.time()
print(factorial(100))
finish2 = time.time()

print(f"factorial execution: {finish2-start2}")






def timer(func):
    def clocked(*args):
        start = time.time()
        result = func(*args)
        finish = time.time()
        print(f"{func.__name__} execution: {finish-start:.5f}")
        return result
    return clocked

def clock(func):
    def clocked(*args):
        start = time.perf_counter()
        result = func(*args)
        finish = time.perf_counter()
        elapsed = finish - start
        func_name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f"[{elapsed:.5f}] {func_name}({arg_str}) -> {result}")
    return clocked

@clock
def fibo(value):
    fibo_dict = dict()
    a, b = 0, 1
    for item in range(1, value+1):
        a, b, = b, a + b
        fibo_dict[item] = a
    return fibo_dict


@clock
def factorial(n):
    i = n
    while i > 1:
        i -= 1
        n *= i
    return n


@clock
def snooze(seconds):
    time.sleep(seconds)


fibo(50)
factorial(100)
snooze(0.5)