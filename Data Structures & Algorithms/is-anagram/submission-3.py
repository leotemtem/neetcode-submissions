class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        for letter in t:
            if letter not in letters:
                return False
            letters[letter] -= 1
        for amount in letters.values():
            if amount != 0 :
                return False
        return True

        