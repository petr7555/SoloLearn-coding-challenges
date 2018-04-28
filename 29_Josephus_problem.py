def josep(n):
    people = []
    for i in range(1,n+1):
        people.append(i)
    x = 0
    y = 0
    while len(people) != 1:
        print("people:", people)
        x = (x + 1) % len(people)
        print("person",people[x-1]," kills:", people[x])
        people.remove(people[x])
    return ("survivor: " + str(people[0]))


print(josep(24))
