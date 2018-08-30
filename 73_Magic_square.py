matrix3 = [[4,3,8],
          [9,5,1],
          [2,7,6]]
matrix4 = [[8,11,14,1],
           [13,2,7,12],
           [3,16,9,6],
           [10,5,4,15]]
matrix5 = [[17,24,1,8,15],
           [23,5,7,14,16],
           [4,6,13,20,22],
           [10,12,19,21,3],
           [11,18,25,2,9]]

def magic(m):
    #check if square
    for i in range(len(m)):
        if len(m) != len(m[i]):
            return("not a square matrix")
    size = len(m)
    s = sum(m[0])
    #check rows
    for i in range(size):
        if sum(m[i]) != s:
            return False
    #check columns
    for i in range(size):
        c = 0
        for j in range(size):
            c += m[j][i]
        if c != s:
            return False
    #check diagonals
    c = 0
    for i in range(size):
        c += m[i][i]
    if c != s:
        return False

    c = 0
    for i in range(size):
        c += m[i][size-i-1]
    if c != s:
        return False
    
    return(s)

print(magic(matrix3))
print(magic(matrix4))
print(magic(matrix5))
