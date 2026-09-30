class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # You cannot turn back time
        
        # New solution: Left and right pointer (it slides!)
        # Create a left pointer and right pointer, set both to index 0 and 1
        # IF Right Pointer is less than Left Pointer, update the Left Pointer
            # to be the Right Pointer and Right Pointer shifts over by 1
            # Basically, slide the two pointers over
        # ELSE Right Pointer is more than Left Pointer
            # Calculate difference. Store if bigger than maxProfit
            # Slide right pointer over by 1
        
        # Can there be two of the same number?
        # Can there be negative numbers?

        # Create a maxProfit variable to store the number
        maxProfit = 0
        leftPointer = 0
        rightPointer = 1

        # This will only iterate through the entire list once:
        # Giving it O(n) time
        while rightPointer < len(prices):
            if prices[leftPointer] > prices[rightPointer]:
                leftPointer = rightPointer
                rightPointer += 1
            elif prices[leftPointer] < prices[rightPointer]:
                difference = prices[rightPointer] - prices[leftPointer]
                if difference > maxProfit:
                    maxProfit = difference
                rightPointer += 1
            elif prices[leftPointer] == prices[rightPointer]: # edge case
                rightPointer += 1
    
        # return maxProfit
        return maxProfit