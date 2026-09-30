# General idea:
# The eating speed shouldn't exceed the max number of bananas
# in any pile since you can only eat from one pile per hour

# We can start a binary search of 1 banana/hr to max banana/hr
# If we finish all the piles under the given number of hours, we should
# eat less bananas per hour
# If we cannot finish all the piles within the given number of hours, 
# we should eat more bananas per hour

# Do this until you find the perfect bananas/hr that will minimize
# the number of bananas you eat per hour AND finish all the piles

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftPointer = 1
        rightPointer = max(piles)
        result = rightPointer # worst case

        while leftPointer <= rightPointer:
            middlePointer = (leftPointer + rightPointer) // 2
            hours = 0 # to eat all bananas
            for pile in piles:
                # MiddlePointer is the designated number of bananas
                # See how many hours it takes to eat from this pile at the
                # given rate, rounded up 
                hours += math.ceil(pile / middlePointer)

            # If the number of hours taken is smaller or equal to 
            # the number of hours given:
            # Basically, if the answer is valid:
            if hours <= h:
                result = min(result, middlePointer)
                # Eliminate half the search scope
                rightPointer = middlePointer - 1
            # If the answer is not valid
            else:
                # Eliminate half the search scope
                leftPointer = middlePointer + 1
        
        return result
