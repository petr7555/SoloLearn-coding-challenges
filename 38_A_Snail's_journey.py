import math
def snail(H, A, B):
    return math.ceil((H-B)/(A-B))

print(snail(15,1,0.5))