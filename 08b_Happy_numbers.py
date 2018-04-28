def happy(n, orig):
    sum = 0
    for c in n:
        sum += int(c)**2
    if sum == 1:
        print(orig)
    elif sum == 4:
        return
    else:
        return (happy(str(sum), orig))

    
ran = input()
for number in range(1, int(ran) + 1):
    happy(str(number), number)
