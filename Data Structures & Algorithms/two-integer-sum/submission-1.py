class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            deff = target - i
            for j in range(nums.index(i)+1, len(nums)):
                if (deff == nums[j]):
                    return [nums.index(i), j]