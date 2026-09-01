class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        # map_s, map_t = {}, {}
        # for i in range(len(s)):
        #     map_s[s[i]] 
        #     if s[i] != t[i]:
        #         return False
        if s == t:
            return True
        return False