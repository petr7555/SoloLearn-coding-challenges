n = int(input())
print("{} is".format(n)+ ("" if str(n**3)[-len(str(n)):]==str(n) else " not") + " a trimorphic number")
print("{} is".format(n)+ ("" if str(n**3).endswith(str(n)) else " not") + " a trimorphic number")
