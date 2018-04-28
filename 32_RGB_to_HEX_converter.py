def rgb(t):
    dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F",}
    hex = []
    for i in range(3):
        temp = []
        for j in range(2):
            if t[i] % 16 > 9:
                temp.append(dict[t[i] % 16])
            else:
                temp.append(t[i] % 16)
            t[i] = t[i] // 16
        for i in range(2):
            hex.append(str(temp.pop()))
    return "#" + "".join(hex)

print(rgb([4, 15, 33]))
