class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num = 0
        if len(s) != len(t):
            return False
            num = 1
        else:
            for a in s:
                count1 = s.count(a)
                count2 = t.count(a)
                if count1 != count2:
                    return False
                    num = 1
        if num == 0:
            return True