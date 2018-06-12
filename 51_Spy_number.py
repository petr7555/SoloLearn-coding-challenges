"""inp = input()
count = 0
product = 1
for c in inp:
    count += int(c)
    product *= int(c)
if count == product:
    print("Spy number!")
else:
    print("Not a spy number.")"""

def spy(n):
    spyl = []
    for i in range(n+1):
        count = 0
        product = 1
        for c in str(i):
            count += int(c)
            product *= int(c)
        if count == product:
            spyl.append(i)
    return spyl

print(spy(10000))
