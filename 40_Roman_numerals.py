def roman(n):
    string = ""
    
    for i in range(n // 1000):
        string += "M"
    n %= 1000
    
    if n // 100 == 9:
        string += "CM"
        n %= 100
    else:
        for i in range(n // 500):
            string += "D"
        n %= 500
        
        for i in range(n // 100):
            string += "C"
        n %= 100

    if n // 10 == 9:
        string += "XC"
        n %= 10
    else:    
        for i in range(n // 50):
            string += "L"
        n %= 50
    
        for i in range(n // 10):
            string += "X"
        n %= 10

    if n == 9:
        string += "IX"
    else:
        for i in range(n // 5):
            string += "V"
        n %= 5
    
        for i in range(n // 1):
            string += "I"
    
    return string

print(roman(1988))
