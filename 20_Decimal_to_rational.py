def rational(n):
    dot_pos = n.find(".")
    d = 1
    for i in range(1, len(n) - dot_pos):
        d *= 10
    c = int(n[dot_pos+1:])
    divided = True
    while divided:
        divided = False
        for num in range(2,c+1):
            if c % num == 0 and d % num == 0:
                c = c // num
                d = d // num
                divided = True
                break
    string = str(c) + " / " + str(d)
    return string

print(rational(input()))




