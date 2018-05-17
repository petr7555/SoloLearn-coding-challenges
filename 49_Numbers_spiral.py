def spiral(n):
    arr = [[0 for i in range(n)] for i in range(n)]
    mid_x = n // 2
    mid_y = n // 2
    m = 1
    arr[mid_x][mid_y] = m
    m += 1
    arr[mid_x][mid_y-1] = m
    m += 1
    arr[mid_x+1][mid_y-1] = m
    m += 1
    arr[mid_x+1][mid_y] = m
    m += 1
    arr[mid_x+1][mid_y+1] = m
    m += 1
    arr[mid_x][mid_y+1] = m
    m += 1
    arr[mid_x-1][mid_y+1] = m
    m += 1
    arr[mid_x-1][mid_y] = m
    m += 1
    arr[mid_x-1][mid_y-1] = m
    """biggest = n*n
    for i in range(len(arr[0])):
        arr[0][i] = biggest - i
    for i in range(len(arr[n-1])):
        arr[n-1][i] = biggest - i"""
    
    for i in range(len(arr)):
        for j in arr[i]:
            print(j, end=" ")
        print()
    print(mid_x, mid_y)
spiral(3)
