dic = {0: "0",
     1: "1",
     2: "2",
     3: "3",
     4: "4",
     5: "5",
     6: "6",
     7: "7",
     8: "8",
     9: "9",
     }
n = 3.14
k = n
d = 0

"""zjistí počet des. míst"""
while k//1 != k:
    k = k * 10
    d += 1
k = n*(10**d)
i = 0
"""zjistí počet cifer"""
while k//10 != 0: 
    k = k//10
    i += 1
k = n*(10**d)
s = []
"""po jednotlivých číslech vkládá do listu"""
for j in range(i, -1,-1):
    if j == d-1:
        s.append(".")
    m = 10**j
    s.append(dic[k//m])
    k = k - k//m * m
snum = "".join(s)
print(snum, type(snum))
