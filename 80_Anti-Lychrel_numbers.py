def lychrel(n):
    for i in range(30):
        print("{} + {} = {}".format(n, reverse(n), n+reverse(n)))
        if palindrome(n+reverse(n)):
            return True
        else:
            n = n+reverse(n)        
    return False

def reverse(n):
    return int(str(n)[::-1])

def palindrome(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            return False
    return True

print(lychrel(12))
print(lychrel(57))
print(lychrel(10911))
