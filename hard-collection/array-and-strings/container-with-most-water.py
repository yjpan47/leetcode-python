class Solution(object):
    def maxArea(self, height):
        N = len(height)
        l = 0
        r = N - 1
        maximum = None
        while l < r:
            left = height[l]
            right = height[r]
            cap = min(left, right) * (r - l)
            maximum = max(cap, maximum) if maximum is not None else cap
            if left < right:
                l += 1
            else:
                r -= 1
        return maximum