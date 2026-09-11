from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0

        for i in sentences:
            x = len(i.split())
            if x > ans:
                ans = x

        return ans  
