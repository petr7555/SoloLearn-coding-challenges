def plane(x,y, x1, y1, x2, y2):
    p = []
    for i in range(2*y+2):
        p.append([])
        for j in range(4*x+2):
            p[i].append(" ")
    p[0][2*x-2] = "y"
    p[0][2*x] = "^"
    for l in range(1,y+1):
        p[l][2*x] = "|"
    for r in range(x):
        p[y+1][r] = "--"
    p[y+1][x] = "|"
    for r in range(x+1,2*x+1):
        p[y+1][r] = "--"
    p[y+1][2*x+1] = ">"
    p[y+2][2*x] = "|"
    p[y+2][4*x+1] = "x"
    for l in range(y+2,2*y+2):
        p[l][2*x] = "|"

    p[y+1-y1][2*x+2*x1]="*"
    p[y+1-y2][2*x+2*x2]="*"
    
    for i in range(len(p)):
        print("".join(p[i]))    

def car(s):
    coord = []
    minus = ""
    for c in s:
        if c.isdigit():
            coord.append(int(minus+c))
        elif c == "-":
            minus = "-"
        else:
            minus = ""
    x1, y1, x2, y2 = coord
    dist = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    
    plane(max(abs(x1),abs(y1),abs(x2),abs(y2))+1, max(abs(x1),abs(y1),abs(x2),abs(y2))+1, x1, y1, x2, y2)
    return dist

print("Distance is:", car("(2,2)(-3,-4)"))

