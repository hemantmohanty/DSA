class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for opp in operations:
            if opp in ("++X", "X++"):
                x += 1
            else:
                x -= 1
        return x
