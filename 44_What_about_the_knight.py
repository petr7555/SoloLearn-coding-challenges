def knight(horse):
    s = 0
    r = ord(horse[0])-97
    c = int(horse[-1])-1
    indices = [[r-2, c-1], 
               [r-2, c+1],
               [r-1, c+2], 
               [r+1, c+2],
               [r+2, c+1], 
               [r+2, c-1],
               [r+1, c-2], 
               [r-1, c-2]] 
    for pair in indices:
        if pair[0] in range(0,8) and pair[1] in range(0,8):
            s += 1
    return s

print(knight("g6"))
