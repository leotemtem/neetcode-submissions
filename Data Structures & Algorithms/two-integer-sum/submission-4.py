class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()
        for index, number in enumerate(nums):
            compliment = target - number
            if compliment in numbers:
                return [numbers[compliment],index]
            numbers[number] = index
