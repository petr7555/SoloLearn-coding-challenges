def multiplyf(a,b,c,d):
    real = a*c - b*d
    imaginary = a*d+b*c
    if imaginary < 0:
        result = "{} - {}i".format(real, abs(imaginary))
    else:
        result = "{} + {}i".format(real, imaginary)
    return result

print(multiplyf(1,2,3,4))
print(multiplyf(1,-2,3,4))

def multiply(a,b,c,d):
    real = a*c - b*d
    imaginary = a*d+b*c
    return real, imaginary

def divide(a,b,c,d):
    real, imaginary = multiply(a,b,c,-d)
    divisor = c**2+d**2
    real = real/divisor
    imaginary = imaginary/divisor
    if imaginary < 0:
        result = "{} - {}i".format(real, abs(imaginary))
    else:
        result = "{} + {}i".format(real, imaginary)
    return result

print(divide(1,2,3,4))
print(divide(1,-2,3,4))
