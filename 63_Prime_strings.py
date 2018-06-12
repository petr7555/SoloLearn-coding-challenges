def prime(s):
    l = len(s)
    for i in range(1,l//2+1):
        groups = []
        if l%i == 0:
            group_len = i
            for j in range(0, l, group_len):
                groups.append(s[j:j+group_len])
            if len(set(groups)) == 1:
                return "not prime"
    return "prime"

tests = ["abac","xyxy", "aaaa", "hello", "aa", "ababc", "ababab"]
for s in tests:
    print(s, "is", prime(s))
