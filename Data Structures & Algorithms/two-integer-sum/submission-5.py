class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in nums:
                pos = nums.index(sub)
                if pos == i and sub == nums[i]:
                    try:
                        pos = nums.index(sub,pos+1)
                        break
                    except ValueError:
                        continue
                else:
                    break
        return [i, pos]