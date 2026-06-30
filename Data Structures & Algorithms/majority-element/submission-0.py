class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        for num in nums: 
            if num not in elements:
                elements[num] = 0
            elements[num] += 1
        max_element = max(elements, key = elements.get)
        return max_element