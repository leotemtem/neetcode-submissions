class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list(nums)
        for number in nums:
            ans.append(number)
        return ans
        
        