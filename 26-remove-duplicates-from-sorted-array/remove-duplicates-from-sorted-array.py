class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        left = 0
        right = left + 1

        while right < n:
            if nums[left]!=nums[right]:
                left+=1
                nums[left], nums[right] = nums[right], nums[left]
            right+=1
        return left+1