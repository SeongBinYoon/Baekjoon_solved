# 10870 피보나치수5

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return n

n = int(input())
res = fib(n)
print(res)