class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = dict()
        for word in strs:
            anagram = ''.join(sorted(word))
            if anagram not in my_dict:
                my_dict[anagram] = []
            my_dict[anagram].append(word)
        return list(my_dict.values())
        