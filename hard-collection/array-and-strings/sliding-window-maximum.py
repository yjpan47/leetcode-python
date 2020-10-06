from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        curr_list = nums[0:k]
        current_max = max(curr_list)
        queue = deque([])
        for i in range(k):
            while len(queue) > 0 and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
                    
        
        l, r = 0, k - 1
        results = [nums[queue[0]]]
        
        while r < len(nums) - 1:
            if queue[0] == l:
                queue.popleft()          
        
            l += 1
            r += 1

            while len(queue) > 0 and nums[r] >= nums[queue[-1]]:
                queue.pop()
            queue.append(r)
            
            results.append(nums[queue[0]])
            
        return results