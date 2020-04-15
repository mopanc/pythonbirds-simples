def soma(*args):
    total = 0
    for n in args:
        total += n
    return total


print(soma())
print(soma(1))
print(soma(1, 2))
print(soma(1, 2, 3))
print(soma(1, 2, 3, 4))



