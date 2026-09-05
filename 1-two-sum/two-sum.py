class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i in range(0, n):
            remening = target - nums[i]
            if remening in seen:
                return [seen[remening], i]
            seen[nums[i]] = i
