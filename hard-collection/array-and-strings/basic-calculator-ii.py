class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        num = 0
        sign = '+'
                
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            if (i == len(s) - 1) or (char == '+' or char == '-' or char == '/' or char == '*'):
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                if sign == '/':
                    prev = stack.pop()
                    if prev >= 0:
                        stack.append(prev // num)
                    else:
                        stack.append(-((-prev) // num))
                sign = char
                num = 0
        
        value = sum(stack)
        return value