class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create hash map [value, index]
        map = {}

        # Find the difference and check if it exists in map
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in map:
                return [map[difference], i] # guaranteed to hit
            
            map[nums[i]] = i
