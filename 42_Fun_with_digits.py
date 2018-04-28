operators = ["+","-"]
target = 100

lines = ["1"]
for i in range(2,10):
    for j in range(len(lines)):
        for op in operators:
            lines.append(lines[j]+op+str(i))
        lines[j] += str(i)
c = 0
for line in lines:
    if eval(line) == target:
        print(line,"=",target)


