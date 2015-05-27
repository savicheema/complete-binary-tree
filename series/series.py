import math, random

def diff_series(diff, limit):
    result = []
    num = 1
    while num < limit:
        result.append(num)
        num = num + diff
    return result

def fibonacci(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    series = diff_series(4, 52)
    for num in series:
        print num
