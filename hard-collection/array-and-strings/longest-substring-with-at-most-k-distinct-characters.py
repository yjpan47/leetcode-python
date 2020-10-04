class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if k == 0 or n == 0:
            return 0
        hashmap = {}
        left, right = 0, 0
        max_length = 0
        while right < n:
            char = s[right]
            hashmap[char] = hashmap.get(char, 0) + 1
            if (right + 1 == n) or (s[right + 1] not in hashmap and len(hashmap) == k):
                max_length = max(max_length, right - left + 1)
                while (left <= right and len(hashmap) == k):
                    char = s[left]
                    hashmap[char] -= 1
                    if hashmap[char] == 0:
                        del hashmap[char]
                    left += 1
            right += 1
        return max_length