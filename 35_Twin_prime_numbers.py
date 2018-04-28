def sieve_twin(m,n):
    list = []
    for i in range(2, n+1):
        list.append(i)
    j = 0
    while j < len(list):
        p = list[j]
        x = 2
        while x*p <= list[-1]:
            if x*p in list:
                list.remove(x*p)
            x += 1
        j += 1
    cleared_list = list[:]
    for p in list:
        if p < m:            
            cleared_list.remove(p)
    result = []
    for i in range(len(cleared_list)-1):
        if cleared_list[i] == cleared_list[i+1] - 2:
            result.append((cleared_list[i],cleared_list[i+1]))
    return result

print(sieve_twin(0,15))
