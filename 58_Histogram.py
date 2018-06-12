import operator
import copy
inp = [2,5,2,3,4,5,1,5,3,3,4]
inp.sort()
mean = sum(inp)/len(inp)
d = {}
for n in inp:
    d[n] = d.get(n,0) + 1
dict = copy.copy(d)
modes = []
mode = max(dict.items(), key=operator.itemgetter(1))[0]
count = dict[mode]
modes.append(mode)
dict.pop(mode)
while dict[max(dict.items(), key=operator.itemgetter(1))[0]] == count:
    mode = max(dict.items(), key=operator.itemgetter(1))[0]
    modes.append(mode)
    dict.pop(mode)
if len(inp)%2 != 0:
    median = inp[len(inp)//2]
else:
    median = (inp[len(inp)//2-1]+inp[len(inp)//2])/2

print("Mean: {:.2f}".format(mean))
print("Mode:", ", ".join(map(str,modes)))
print("Median:", median)
print("Histogram: ")
for i in d:
    print (i,"| ",end = "")
    for j in range(d[i]):
        print("*",end="")
    print()
