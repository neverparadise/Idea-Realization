class Averager():

    def __init__(self) -> None:
        self.series = []

    def __call__(self, new_value: float) -> float:
        self.series.append(new_value)
        total = sum(self.series)
        avg = total/len(self.series)
        print(avg)
        return avg
    
avg = Averager()
avg(10)
avg(11)
avg(12)


def make_averager():

    # Closure -----------------------------
    series = []
    
    def averager(new_value):
        series.append(new_value) # 중첩된 함수에서 외부변수를 참조 -> 자유변수
        total = sum(series)
        avg = total/len(series)
        print(avg)
        return avg
    
    # Closure -----------------------------

    return averager

avg = make_averager()
avg(10)
avg(11)
avg(12)
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__[0].cell_contents)


def make_averager():
    count = 0
    total = 0
    
    def averager(new_value):
        nonlocal count, total 
        count += 1
        total += new_value
        return total / count
    
    return averager