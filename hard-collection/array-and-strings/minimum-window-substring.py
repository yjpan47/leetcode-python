class Solution(object):
    def minWindow(self, s, t):
        t_dict = {}
        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1
        s_dict = {}
        i = 0
        j = 0
        required = len(t_dict)
        formed = 0
        ans = float("inf"), None, None
        while j < len(s):           
            character = s[j]
            s_dict[character] = s_dict.get(character, 0) + 1
            if character in t_dict and s_dict[character] == t_dict[character]:
                formed += 1
            while i <= j and formed == required:
                if j - i + 1 < ans[0]:
                    ans = j - i + 1, i, j 
                character = s[i]
                s_dict[character] -= 1
                if character in t_dict and s_dict[character] < t_dict[character]:
                    formed -= 1
                i += 1
            j += 1
        if ans[0] != float("inf"):
            return s[ans[1]:ans[2] + 1]
        else:
            return ""