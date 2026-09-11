class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0] 
        for index, char in enumerate(answer):
            for word in strs[1:]:
                if index == len(word) or word[index] != char:
                    return answer[:index]
        return answer

            