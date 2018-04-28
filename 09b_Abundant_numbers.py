ran = int(input())

for n in range(1, ran+1):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    if sum > 2*n:
        print(n)
