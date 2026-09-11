class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = dict()
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1
            if frequency[num] > (len(nums)/2):
                return num
        