def json(S1,S2):
    diffs = []
    s1 = list(map(str.strip, S1.split(",")))
    s2 = list(map(str.strip,S2.split(",")))
    if len(s1) >= len(s2):
        longer = len(s1)
    else:
        longer = len(s2)
    for i in range(longer):
        if s1[i] != s2[i]:
            if i == 0:
                diffs.append(s1[i][1:]+"\n"+s2[i][1:])
            elif i == longer-1:
                diffs.append(s1[i][:-1]+"\n"+s2[i][:-1])
            else:
                diffs.append(s1[i]+"\n"+s2[i])
    for diff in diffs:
        print(diff)
        print()

json("{\"a\":2, \"b\":3}","{\"a\":2, \"b\":4}")
json("{\"a\":hello, \"b\":{\"c\": 3}}","{\"a\":hello, \"b\":{\"c\": 11}}")
json("{\"a\":3, \"b\":3}","{\"a\":2, \"b\":3}")
json("{\"a\":2, \"b\":3, \"c\":3}","{\"a\":2, \"b\":4, \"c\":3}")
json("{\"a\":2, \"b\":3, \"c\":3}","{\"a\":2, \"b\":4, \"c\":7}")
