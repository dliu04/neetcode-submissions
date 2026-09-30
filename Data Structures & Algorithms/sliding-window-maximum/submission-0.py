class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = list()
        
        # Condition where bums is less than or equal k
        if len(nums) <= k:
            res.append(max(nums))
            return res

        leftPointer = 0
        rightPointer = k - 1

        while rightPointer < len(nums):
            # leftPointer inclusive, rightPointer exclusive
            res.append(max(nums[leftPointer : rightPointer + 1]))
            rightPointer += 1
            leftPointer += 1
            
        return res