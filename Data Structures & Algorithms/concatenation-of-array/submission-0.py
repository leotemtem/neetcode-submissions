class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        for x in range(len(nums)): 
            ans.append(nums[x])
        return ans