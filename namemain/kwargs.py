def myfunc(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f'key: {k}, value: {v} ')

my_dict = {'1': 'RL^2', '2': 'MAML'}
print(my_dict)
print(myfunc(one=1, two=2))
myfunc(**my_dict)
