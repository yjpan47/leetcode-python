# Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [0] * n
        prod = 1
        for i in range(n):
            result[i] = prod
            prod = prod * nums[i]
        prod = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * prod
            prod = prod * nums[i]
        return result