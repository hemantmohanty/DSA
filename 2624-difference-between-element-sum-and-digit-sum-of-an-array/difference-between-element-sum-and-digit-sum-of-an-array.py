class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        s1 = 0
        s2 = 0
        for i in nums:
            s1 += i
            if len(str(i)) == 1:
                s2+=i
            else:
                for j in str(i):
                    s2 +=int(j)
        return abs(s1-s2)
            
        