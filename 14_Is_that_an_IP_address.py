inp = input().split(".")
print (".".join(inp), "-", "valid" if all(i.isnumeric() and 0 <= int(i) < 256 and len(i) <= 3 for i in inp) and len(inp) == 4 else "invalid")
