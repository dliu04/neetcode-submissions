class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Does the array Numbers have any duplicate values?
        leftPointer = 0
        rightPointer = 0
        solutionFound = False

        # Since there will always be one valid solution, we can utilize
        # a while loop.
        while solutionFound == False:
            # iterate through right pointer from starting to len(numbers)
            for rightPointer in range(leftPointer + 1, len(numbers)):
                if ((numbers[leftPointer] + numbers[rightPointer]) == target and
                    leftPointer != rightPointer):
                    solutionFound = True
                    return [leftPointer + 1, rightPointer + 1]

            leftPointer += 1

        # 1-indexed, so make sure you return the index + 1
        # Does it matter what order the index is? Can we return [2,1] for example?

        # We know the program has failed if this occurs
        return [0,0]