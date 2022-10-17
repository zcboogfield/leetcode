#Runtime: 6129 ms, faster than 5.23% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
#Memory Usage: 21.3 MB, less than 31.39% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
from math import floor
class Solution:
    def canThreePartsEqualSum(self, arr):
        division = sum(arr) / 3
        frontCheck = 0
        backCheck = 0
        mid = [0,0]
        if floor(division) == division:
            for ind, val in enumerate(arr):
                if sum(arr[0:ind]) == division and not frontCheck:
                    frontCheck = ind 
                    mid[0] = ind + 1
                if sum(arr[0:len(arr) - ind]) == division and not backCheck: 
                    backCheck = len(arr) - ind 
                    mid[1] = len(arr) - ind - 1
                if frontCheck and backCheck:
                    return sum(arr[mid[0] : mid[1]]) == division and arr[0: frontCheck] + arr[mid[0] : mid[1]] + arr[] == arr and len(arr[mid[0]: mid[1]])
        return False


run = Solution()

print('test')
print('test')
#print(run.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1],) == True)
#print(run.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]) == False)
#print(run.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]) == True)
print(run.canThreePartsEqualSum([1,-1,1,-1]) == False)


