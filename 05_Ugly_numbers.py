def ugly_rec(n):
    if n == 1:
        return True
    elif n%2 == 0:
        return ugly_rec(n//2)
    elif n%3 == 0:
        return ugly_rec(n//3)
    elif n%5 == 0:
        return ugly_rec(n//5)
    else:
        return False

print(ugly_rec(int(input())))
