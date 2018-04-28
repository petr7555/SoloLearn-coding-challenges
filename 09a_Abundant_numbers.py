n = int(input())
factors = []
sum = 0
for i in range(1, n+1):
    if n % i == 0:
        sum += i
        factors.append(i)
print("Factors are: ", factors)
print("Sum is: ", sum)
if sum > 2*n:
    print("Abundant number!")
else:
    print("Not an abundant number!")
