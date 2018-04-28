def auto(n):
    square = n**2
    if str(square)[-len(str(n)):] == str(n):
        return True
    return False

def all_auto(r):
    nums = []
    for n in range(1,r+1):
        square = n**2
        if str(square)[-len(str(n)):] == str(n):
            nums.append(n)
    return nums

print(all_auto(500000))
