def notate(m):
    c = 0
    n = abs(m)
    if n > 1:
        while n / 10 > 1:
            n = n / 10
            c += 1
    elif n < 1:
        while n < 1:
            n = n * 10
            c -= 1
    if m < 0:
        print ("-{} * 10^{}".format(n, c))
    else:
        print ("{} * 10^{}".format(n, c))

notate(9000000)
notate(0.00006564)
notate(-9000000)
notate(-0.00006564)
