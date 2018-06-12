import itertools

def pair(inp):
    nums = [1,2,4,4]
    for c in itertools.combinations(nums,2):
        if sum(c) == inp:
            return True
    return False

#print(pair(int(input())))

def pairn(inp):
    nums = [1,2,4,4,-1]
    for i in range(len(nums)):
        if inp-nums[i] in nums[i+1:]:
            return ("["+str(nums[i])+", "+str(inp-nums[i])+"]")
    return False

print(pairn(int(input())))
