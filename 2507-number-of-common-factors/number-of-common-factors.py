class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        while b != 0:
            rem = a % b
            a = b
            b = rem
        count = 0

        for i in range (1, a + 1):
            if a % i == 0:
                count +=1
        return count
        