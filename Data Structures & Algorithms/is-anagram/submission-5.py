class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myDict = dict()
        for letter in s:
            if letter not in myDict:
                myDict[letter] = 1
            else:
                myDict[letter] += 1
        for letter in t:
            if letter not in myDict:
                return False
            else:
                myDict[letter] -= 1
        for val in myDict.values():
            if val != 0 :
                return False
        return True 
        