import random

def box():
    boxes = gen()
    for box in boxes:
        if box < 10 or box > 20:
            return boxes, "index of box:", boxes.index(box)

def gen():
    boxes = []
    for i in range(99):
         boxes.append(random.randint(10, 20))
    random_weight = [random.randint(1, 9),random.randint(21, 99)]
    boxes.insert(random.randint(0, 99), random_weight[random.randint(0,1)])
    return boxes

print(box())
