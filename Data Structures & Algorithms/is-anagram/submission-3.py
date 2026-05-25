class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sort_s = sorted(s)
            sort_t = sorted(t)
            if sort_s != sort_t:
                return False
            else:
                return True