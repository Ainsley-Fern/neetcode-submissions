class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num = 0
        if len(s) != len(t):
            return False
            num = 1
        else:
            sort_s = sorted(s)
            sort_t = sorted(t)
            if sort_s != sort_t:
                return False
                num = 1
        if num == 0:
            return True