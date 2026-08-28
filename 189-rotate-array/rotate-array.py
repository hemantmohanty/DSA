class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        start = 0
        end = len(nums)-1

        while end > start:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        start = 0
        end = k-1
        while end > start:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        start = k
        end = len(nums) - 1
        while end > start:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        return nums


        