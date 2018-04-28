def garland(word):
    g = 0
    for i in range(len(word)):
        if word[:i] == word [-i:]:
            g = i
    return word[:g], g

words = "abracadabra", "tomato", "python", "a", "aa", "ab", "aaa", "aba", "aab"

for word in words:
    gar = garland(word)
    print("{} is {}a garland word {}".format(word, "not " * (gar[0] == ""), ("of a degree of " + str(gar[1]) + ": " + gar[0])*(gar[0] != "")))
