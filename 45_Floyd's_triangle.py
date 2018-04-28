def floyd(n):
    n = 8
    c = 0
    print("Floyd's triangle:")
    for i in range(1,n+1):
        for j in range(i):
            c += 1
            print (c, end=' ') 
        print() 

    print("\nReverse Floyd's triangle:")

    k = (n+1)*n//2+1
    for i in range(n, 0, -1):
        for j in range(i):
            k -= 1
            print (k, end=' ') 
        print()

floyd(5)
