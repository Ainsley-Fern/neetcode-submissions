class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_count= len(set(nums))
        if unique_count == len(nums):
            ans = False
        else:
            ans = True

        return ans