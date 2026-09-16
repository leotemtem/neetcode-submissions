class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for word in strs:
            current = "".join(sorted(word))
            if current not in anagrams:
                anagrams[current] = []
            anagrams[current].append(word)
        return list(anagrams.values())
        