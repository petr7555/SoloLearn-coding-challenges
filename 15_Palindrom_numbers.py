def palindrom(n):
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True

print(palindrom(input()))
