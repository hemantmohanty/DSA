class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sumOfDigits = 0

        for i in str(n):
            d = int(i)
            product*=d
            sumOfDigits+=d

        return product - sumOfDigits

        