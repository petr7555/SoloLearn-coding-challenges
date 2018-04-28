def find(n, d):
    results = [] 
    for i in range(n):
        if str(d) in str(i):
            results.append(str(i)) 
    return ", ".join(results) 

print(find(300,42))