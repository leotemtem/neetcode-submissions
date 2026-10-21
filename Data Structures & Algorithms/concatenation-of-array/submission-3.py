class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr : list = list(nums) 
        for num in nums:
            arr.append(num)
        return arr

        