class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        # Pretend the arrays are merged.
        # Find the Total and the Half of the merged array
        # Half tells us the number of elements in the left partition
        total = len(nums1) + len(nums2)
        half = total // 2

        # Run binary search only on the smaller array
        # Make sure A is always the smaller one
        if len(B) < len(A):
            A, B = B, A # Switch them


        leftPointer = 0
        rightPointer = len(A) - 1
        while True: # There is guaranteed a median so once we find it we can just return it
            # Get A's left partition
            i = (leftPointer + rightPointer) // 2

            # Get B's left partition index
            # (i + 1) + (j + 1) = half
            # isolate j to get the index
            j = half - i - 2

            # Get the element that splits the array in half (left) and
            # the next element we are comparing it to (right)
            # if i is still in bounds (for edge cases)
            Aleft = A[i] if i >= 0 else float("-infinity")
            # If A[i + 1] is not in bounds, we want all values in array A to be in left partition
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") # Too far to the right
            # if j is still in bounds
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # If each array's ending element is less than the other's array
            # midpoint incremented by one (middle of the road!):
            if Aleft <= Bright and Bleft <= Aright:
                # If we have an odd number of elements
                if total % 2:
                    return min(Aright, Bright)
                    # In cases like (4, infinity) we take the minimum value so it works)
                # If it is even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # Else if the search is incomplete
            # too big
            elif Aleft > Bright:
                rightPointer = i - 1 # Reduce the size of the left partition for A
            # Aleft <= bRight (too small)
            else:
                leftPointer = i + 1
