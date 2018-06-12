def pattern1(n):
    num = 1
    for i in range(1, n+1):
        line = ""
        for j in range(i):            
            line += str(num**2) + " "
            num += 1
        print (line)
    return "DONE"

print(pattern1(5))

def pattern2(n):
    num = 0
    b = 0
    for i in range(1, n+1):
        line = ""
        for j in range(i):            
            num += 1
        a = num
        while a > b:
            line += str(a) + " "
            a -= 1
        b = num
        print (line)
    return "DONE"

#print(pattern2(5))

def pattern3(n):
    num = 65
    for i in range(1, n+1):
        line = ""
        for j in range(i):            
            line += chr((num - ord("A"))%26 + ord("A")) + " "
            num += 1
            line += chr((num - ord("A"))%26 + ord("A")) + " "
            num += 1
        print (line)
    return "DONE"

#print(pattern3(5))

def pattern4(n):
    middle= n//2
    for i in range(middle):
        line = ""
        for j in range(i+3):
            line += "#"
        print (line)
    for i in range(n - middle, 0, -1):
        line = ""
        for j in range(i+2):
            line += "#"
        print (line)
    return "DONE"

#print(pattern4(5))

def pattern5(n):
    middle= n//2
    for i in range(middle, 0, -1):
        line = ""
        for j in range(i+3 + n%2 - 1):
            line += "#"
        print (line)
    for i in range(n - middle):
        line = ""
        for j in range(i+3):
            line += "#"
        print (line)
    return "DONE"

#print(pattern5(7))

"""reversed"""

def pattern1_r(n):
    list = []
    num = 1
    for i in range(1, n+1):
        line = ""
        for j in range(i):            
            line += str(num**2) + " "
            num += 1
        list.append(line)
    for i in range(1,len(list)+1):
        print(list[-i])
    return "DONE"

#print(pattern1_r(5))

def pattern2_r(n):
    list = []
    num = 0
    b = 0
    for i in range(1, n+1):
        line = ""
        for j in range(i):            
            num += 1
        a = num
        while a > b:
            line += str(a) + " "
            a -= 1
        b = num
        list.append(line)
    for i in range(1,len(list)+1):
        print(list[-i])
    return "DONE"

#print(pattern2_r(5))

def pattern3_r(n):
    list = []
    num = 65
    for i in range(1, n+1):
        line = ""
        for j in range(i):            
            line += chr((num - ord("A"))%26 + ord("A")) + " "
            num += 1
            line += chr((num - ord("A"))%26 + ord("A")) + " "
            num += 1
        list.append(line)
    for i in range(1,len(list)+1):
        print(list[-i])
    return "DONE"

#print(pattern3_r(5))
