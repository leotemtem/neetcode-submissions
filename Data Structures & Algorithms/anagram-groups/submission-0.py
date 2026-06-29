class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs: 
            this_word = ''.join(sorted(word))
            if this_word not in anagrams:
                anagrams[this_word] = []
            anagrams[this_word].append(word)
        return list(anagrams.values())