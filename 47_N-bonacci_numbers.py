def fib(n,m):
    if m < 0:
        return 0
    elif m < 2:
        return m
    else:
        sum = 0
        for i in range(n):
            sum += eval("fib(n, m-"+str(i)+"-1)")
        return sum

print(fib(4, 8))
