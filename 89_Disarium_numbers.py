def disarium(n):
    m = list(map(int, list(str(n))))
    result = 0
    for i in range(len(m)):
        result += m[i]**(i+1)
    if result == n:
        return True
    return False

for i in range(1000):
    if disarium(i):
        print(i)
