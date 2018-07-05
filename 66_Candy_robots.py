x = int(input("How many coins do you want to spend?\n"))
n = int(input("How many robots do you have?\n"))

robots = []
for i in range(1,n+1):
    p = int(input("Enter performance of robot number {}.\n".format(i)))
    e = int(input("Enter endurance of robot number {}.\n".format(i)))
    c = int(input("Enter operation cost of robot number {}.\n".format(i)))
    effectivity = round(p/c,2)
    robots.append([i,p,e,c,effectivity])
    
cheapest_robot = min(robots, key = lambda x: x[3])
robots = sorted(robots, key = lambda x: x[4])

total = 0
while x > 0 and len(robots) != 0:
    robot = robots.pop()
    p = robot[1]
    e = robot[2]
    c = robot[3]
    t = 0
    while x-c >= 0 and e > 0:
        e -= 1
        x -= c
        t += 1
    total += t*p
    print("Robot nr. {} will work for {} hours and produces {} candies for {} coins.".format(robot[0], t, t*p, t*c))
    
remaining_coins = x
if x > 0 and x//cheapest_robot[3] > 0:
    rest = x//cheapest_robot[3]
    total += rest
    remaining_coins = x - rest*cheapest_robot[3]
    print("Use robot nr. {} to work for {} more hours. He produces {} candies.".format(cheapest_robot[0],rest,rest))
print("Your robots produced {} candies in total, you have {} coins left.".format(total, remaining_coins))
