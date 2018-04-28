def pan(n):
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    if n[0] == "0":
        n = n[1:]
    for num in nums:
        if num not in n:
            return False
    return True

def pan_h(n):
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    dict = {"0": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,}
    if n[0] == "0":
        n = n[1:]
    for c in n:
        dict[c] += 1
    for num in nums:
        if num not in n:
            return False
    return dict

print(pan_h(input()))

