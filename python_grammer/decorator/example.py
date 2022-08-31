def deco(func): # 함수 객체를 인자로 받습니다. 
    func() 
    def inner():
        print("inner() 함수를 실행중입니다.")
    return inner # 내부의 inner 함수 객체를 리턴합니다. 

@deco
def target():
    print('target() 함수를 실행중입니다. ')

target()
print(target)

# Results
# target() 함수를 실행중입니다. 
# inner() 함수를 실행중입니다.
# <function deco.<locals>.inner at 0x000002877E757948>