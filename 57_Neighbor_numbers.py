inp1 = [12, 13, 15, 19, 212, 556, 2146]
inp2 = [13, 44, 432, 12, 788, 246, 2146, 46]
out = []
for num in inp1:
    if num in inp2:
        out.append(num)
print(out)

print(set(inp1)&set(inp2))
