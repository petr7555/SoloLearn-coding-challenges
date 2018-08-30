def owl(m):
    rows = len(m)
    columns = len(m[0])
    if rows%2 != 0 or columns%2 != 0:
        return False
    for i in range(rows):
        for j in range(columns//2):
            if m[i][j] != m[i][-j-1]:
                return False
    for i in range(columns):
        for j in range(rows//2):
            if m[j][i] != m[-j-1][i]:
                return False
    return True

matrix1 = [["a","b","b","a"],
          ["c","c","c","c"],
          ["c","c","c","c"],
          ["a","b","b","a"]]
matrix2 = [["a","b","d","d","b","a"],
          ["c","z","c","c","z","c"],
          ["c","z","c","c","z","c"],
          ["a","b","d","d","b","a"]]
matrix3 = [["a","b","b","a"],
           ["c","c","c","c"],
           ["c","d","d","c"],
           ["c","d","d","c"],
           ["c","c","c","c"],
           ["a","b","b","a"]]

for i in range(1,4):
    m = "matrix"+str(i)
    exec("print(owl(%s))" % (m))
