def happy(n):
    sum = 0
    for c in n:
        sum += int(c)**2
    print(sum)
    if sum == 1:
        return ("Happy number!")
    elif sum == 4:
        return ("Sad number!")
    else:
        return (happy(str(sum)))

    
number = input()    
print(happy(number))
