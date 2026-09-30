# General idea: Once you have determined a max in a certain window,
# all values that are smaller than the former max are useless 
# and should be ignored.

# Use a queue
# Before pushing current value onto queue, check if anything
# is greater than the current value
# If there exists an value greater than the current value, 
# push the current value onto the stack
# if there does not exist a value greater than the current value,
# pop all other values and push the current value onto the stack

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = list()
        leftPointer = 0
        rightPointer = 0

        # This is a Python double-ended queue (deck)
        # supports efficient pushing and popping 
        # from both ends.
        queue = collections.deque() # the indices of max values (hopefully)

        while rightPointer < len(nums):
            # Make sure no smaller values exist on queue
            # While queue is not empty and 
            # the rightmost value in our queue (queue[-1])
            # is smaller than the current value
            while queue and nums[queue[-1]] < nums[rightPointer]:
                queue.pop()
            # Push current value onto stack
            queue.append(rightPointer)

            # if left value is out of bounds, remove
            # if the leftPointer is > queue's max value index
            # unfortunately we have to remove it
            if leftPointer > queue[0]:
                queue.popleft()

            # If the window is size k
            if (rightPointer + 1) >= k:
                # This works because the leftmost element should always
                # be the biggest element in the window until it gets
                # removed due to window limitations
                res.append(nums[queue[0]])
                # Because rightPointer is now == k, we can 
                # increment leftPointer
                leftPointer += 1

            rightPointer += 1

        return res