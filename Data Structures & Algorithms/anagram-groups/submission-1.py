class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            anagram = ''.join(sorted(word))
            if anagram not in dictionary:
                dictionary[anagram] = []
            dictionary[anagram].append(word)
        return list(dictionary.values())
        