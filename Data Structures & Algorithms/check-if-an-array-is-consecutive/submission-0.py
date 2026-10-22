class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        for i in range(len(sortedNums)-1):
            if (sortedNums[i+1] == sortedNums[i] + 1) :
                continue
            else:
                return False 
        return True