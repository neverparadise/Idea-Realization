

b = 6 # 전역변수
def my_func_local():
    a = 3 # 지역변수
    b = 3
    print(f"local a: {a}")
    print(f"local b: {b}")

def my_func_global():
    global b # b라는 지역변수를 전역변수로 사용한다는 의미
    a = 3 # 지역변수
    b = 3
    print(f"local a: {a}")
    print(f"local b: {b}")

my_func_local()
print(f"global b: {b}")

my_func_global()
print(f"global b: {b}")

# Results (local)
# 3
# 3
# 6

# Results (global)
# 3
# 3
# 3