lower, upper, exp = input().split()
sum = 0
for i in range(int(lower), int(upper)+1):
    sum += eval(str(i) + exp) 
    print(str(i) + exp) 
print(sum) 