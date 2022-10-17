class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for num in range(length):
            already_sorted = True
            for front in range(length - num - 1):
                if nums[front] > nums[front + 1]:
                    nums[front], nums[front + 1] = nums[front + 1], nums[front]
                    already_sort = False
            if already_sorted:
                break

run = Solution()
        
test = [2,0,1]
print(test)
run.sortColors(test) 
print(test)

test = [2,0,2,1,1,0]
print(test)
run.sortColors(test) 
print(test)

