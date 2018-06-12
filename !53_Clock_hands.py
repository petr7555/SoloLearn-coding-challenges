def clock(startTime, endTime):
    startHour = int(startTime[:2])
    startMin = int(startTime[-2:])
    endHour = int(endTime[:2])
    endMin = int(startTime[-2:])
    startTime = startHour + startMin/60
    endTime = endHour + endMin/60
    print(startTime, endTime)
    overlap = 0

    minHand = 0
    hourHand = 0
    angleMin = 6 * startMin
    print(angleMin)
    angleHour = (30 * startTime)%360
    print(angleHour)
    if angleMin == angleHour:
        overlap += 1
    return overlap

print(clock("13:30", "21:20"), "times")
