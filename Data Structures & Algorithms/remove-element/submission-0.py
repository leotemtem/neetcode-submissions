class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        items = 0 
        for num in nums: 
            if num != val:
                nums[items] = num
                items += 1
        return items