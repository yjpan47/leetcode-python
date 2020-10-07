class Solution(object):
    
    def __init__(self):
        self.memo = {}
        
    def recursive_with_memo(self, index, s):
        if index == len(s):
            return 1
        elif int(s[index]) == 0:
            return 0
        else:
            
            if index in self.memo:
                return self.memo[index]
            
            result = self.recursive_with_memo(index + 1, s)
            if index <= len(s) - 2 and int(s[index: index + 2]) <= 26:
                result += self.recursive_with_memo(index + 2, s)
            
            self.memo[index] = result
            
            return result
    
    def numDecodings(self, s):
        return self.recursive_with_memo(0, s)