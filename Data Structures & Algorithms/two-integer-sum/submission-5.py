class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        for index,number in enumerate(nums):
            compliment = target - number
            if compliment in my_dict:
                return [my_dict[compliment],index]
            my_dict[number] = index

        