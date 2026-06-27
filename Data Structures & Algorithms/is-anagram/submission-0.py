class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        if len(s) != len(t):
            return False
        for letter in s: 
            if letter not in dictionary: 
                dictionary[letter] = 0 
            dictionary[letter] += 1 
        for letter in t:
            if letter not in dictionary: 
                return False
            dictionary[letter] -= 1 
        for amount in dictionary.values():
            if amount != 0:
                return False
        return True