class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in anagram_group:
                anagram_group[sorted_word] = []
            anagram_group[sorted_word].append(word)
        return list(anagram_group.values())
        