class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        clean_set = set(nums)
        if len(clean_set) == len(nums):
            ans = False
        else:
            ans = True

        return ans