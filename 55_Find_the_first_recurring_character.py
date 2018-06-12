n = input() or "BCABA"
m = [j for i,j in enumerate(n) if j.lower() in n[:i].lower()]
print(m[0])
