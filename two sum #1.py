def twoSum(nums, target):
    li=[]
    for item in range(len(nums)):
        for i in range(len(nums)):
            if item != i and nums[item] + nums[i] ==target :
                li.append(item)

    return li








print(twoSum([1, 3, 2, 1],2))


