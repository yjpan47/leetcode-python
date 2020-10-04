class Solution(object):
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)
        
        for num in num_set:
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 0
                
                while current_num in num_set:
                    current_num +=1
                    current_streak += 1
                
                longest_streak = max(current_streak, longest_streak)
        
        return longest_streak

    # def longestConsecutive(self, nums):
    #     max_length = 0
    #     n = len(nums)
    #     nums_dict = {}
    #     for i in range(n):
    #         number = nums[i]
    #         nums_dict[number] = nums_dict.get(number, 0) + 1
        
    #     for i in range(n):
    #         curr = nums[i]
    #         value = nums_dict.get(curr)
    #         if value > 0:
    #             print(curr)
    #             nums_dict[curr] -= 1
    #             length = 1
    #             k = 1
    #             while (curr - k) in nums_dict and nums_dict[curr - k] > 0:
    #                 length += 1
    #                 nums_dict[curr - k] -= 1
    #                 k += 1
    #             k = 1    
    #             while (curr + k) in nums_dict and nums_dict[curr + k] > 0:
    #                 length += 1
    #                 nums_dict[curr + k] -= 1
    #                 k += 1
                
    #             max_length = max(max_length, length)
        
    #     return max_length