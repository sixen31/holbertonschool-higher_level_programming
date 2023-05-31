#!/usr/bin/env python3
def add(a, b):
    return a + b


def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result


print(add(1, 2))
print(add(98, 0))
print(add(100, -2))


print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
