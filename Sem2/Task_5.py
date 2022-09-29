# 5. Реализуйте алгоритм перемешивания списка.

l = list(range(30+1))
print(l)

def list_mix(_list):
    x = 1
    size = len(_list)

    for i in range(size):
        m = 2147483647
        a = 16807
        c = 12345
        x = (a * x + c) % m
        # print(f'a = {a}; c = {c}; m = {m}; x = {x}')
        # print(f'x = {x % size}')
        _list[i], _list[x % size] = _list[x % size], _list[i]
    return _list

print(list_mix(l))
