'''
you will have two of one number
and missing one number 
'''

def findErrorNums(nums):
    nums.sort()

    for ind, val in enumerate(nums):
        if val != ind + 1:
            if val == nums[val - 1]:
                return [val, ind + 1]
            elif nums[val - 1] == ind:
                return [nums[val - 1], ind + 1]
            


print(findErrorNums([1,5,3,2,2,7,6,4,8,9]) == [2,10])
print(findErrorNums([3,2,3,4,6,5]) == [3,1])
print(findErrorNums([3,3,1]) == [3,2])
print(findErrorNums([3,2,2]))
#[2,1]
print(findErrorNums([1,2,3,5,5]))
#[5,5]
print(findErrorNums([1,2,2,4]))
#[2,3]
