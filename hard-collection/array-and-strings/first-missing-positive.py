class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            element = abs(nums[i])
            if element <= n:
                nums[element - 1] = abs(nums[element - 1]) * (-1)
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1