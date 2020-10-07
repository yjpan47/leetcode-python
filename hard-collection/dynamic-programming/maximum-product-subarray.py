class Solution(object):
    def maxProduct(self, nums):
        prev_min_product, prev_max_product, max_product = float('inf'), float('-inf'), float('-inf') 
        for n in nums:
            if n == 0:
                prev_min_product, prev_max_product = 0, 0
            elif n < 0:
                prev_min_product, prev_max_product = min(n, prev_max_product * n), max(n, prev_min_product * n)
            else:
                prev_min_product, prev_max_product = min(n, prev_min_product * n), max(n, prev_max_product * n)
            max_product = max(max_product, prev_max_product)
        return max_product