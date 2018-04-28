import random
def conv(n):
    dict = {"0": "zero",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
            "10": "ten",
            "11": "eleven",
            "12": "twelve",
            "13": "thirteen",
            "14": "fourteen",
            "15": "fifteen",
            "16": "sixteen",
            "17": "seventeen",
            "18": "eighteen",
            "19": "nineteen",
            "20": "twenty",
            "30": "thirty",
            "40": "forty",
            "50": "fifty",
            "60": "sixty",
            "70": "seventy",
            "80": "eighty",
            "90": "ninety"}
    
    string = ""
    if int(n) < -99999 or int(n) > 99999:
        return "too big number"
    while len(n) != 0:
        if n[0] == "-":
            n = n[1:]
            string += "minus "
            continue
        if n[0] == "0":
            n = n[1:]
            continue
        if int(n) < 20:
            if string != "" and string[-6:] != "minus ":
                string += "and "
            string += dict[n]
            break
        elif len(n) == 2:
            if string != "" and string[-6:] != "minus ":
                string += "and "
            string+= dict[n[0]+"0"]
            if n[-1] != "0":
                string+= " " + dict[n[-1]]
            break
        elif len(n) == 3:
            string += dict[n[0]] + " hundred "
            n = n[1:]
        elif len(n) == 4:
            string += dict[n[0]] + " thousand "
            n = n[1:]
        elif len(n) == 5:
            if int(n[:2]) < 20:
                string += dict[n[:2]]
            else:
                string+= dict[n[0]+"0"]
                if n[1] != "0":
                    string+= " " + dict[n[1]]
            string += " thousand "
            n = n[2:]    
            
            
    if string == "":
        string = "zero"
    return string

print(conv("-98544"))
"""list = []
for i in range(100):
    ri = random.randint(0,99999)
    list.append(conv(str(ri)))
print(list)"""
