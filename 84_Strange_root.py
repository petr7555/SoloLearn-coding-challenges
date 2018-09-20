def root(n):
    square = list(str((n**2)))
    square_root = list(str(round((n**(1/2)),3)))
    for num in square:
        if num in square_root:
            return True
    return False
    

print(root(11))
print(root(24))
    
