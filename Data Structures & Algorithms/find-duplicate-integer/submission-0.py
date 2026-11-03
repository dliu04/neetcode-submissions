class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Linked list cycle
        # Floyd's algorithm (rabbit and tortoise)

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # ?
            if slow == fast: # if cycle detected
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow