one = ["e","a","i","o","n","r","t","l","s","u"]
two = ["d","g"]
three = ["b","c","m","p"]
four = ["f","h","v","w","y"]
five = ["k"]
eight = ["j","x"]
ten = ["q","z"]

def scrabble(words):
    """takes list of words as input,
    returns a word with the highest score"""
    max = 0
    for word in words:
        points = 0
        for c in word:
            c = c.lower()
            if c in one:
                points += 1
            elif c in two:
                points += 2
            elif c in three:
                points += 3
            elif c in four:
                points += 4
            elif c in five:
                points += 5
            elif c in eight:
                points += 8
            else:
                points += 10
        if points > max:
            max = points
            mv_word = word
    return mv_word

print(scrabble(["This","is","a","cool","Challenge"]))
