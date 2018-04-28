def leyland(n):
    for a in range(2, n//2):
        for b in range(2, n//2):
            if n == a**b + b**a:
                print (True, n)
    return
for i in range(100):
    leyland(i)
