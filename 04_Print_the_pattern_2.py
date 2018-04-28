def pattern1(n):
    for i in range(1,n+1):
        line = ""
        for j in range(i):            
            line += str(i)
        print (line)
    return "DONE"

#print(pattern1(5))

def pattern2(n):
    for i in range(1,n+1):
        line = ""
        for j in range(1,i+1):            
            line += str(j)
        print (line)
    return "DONE"

#print(pattern2(5))

def pattern3(n):
    for i in range(1,n+1):
        line = ""
        for j in range(1,2*i,2):            
            line += str(j)
        print (line)
    return "DONE"

#print(pattern3(5))

def pattern4(n):
    for i in range(1,n+1):
        line = ""
        for j in range(i):            
            line += str(j%2)
        print (line)
    return "DONE"

#print(pattern4(5))
