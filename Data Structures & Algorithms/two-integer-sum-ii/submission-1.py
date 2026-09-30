class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # If an array is pre-sorted, think about how you can use that
        # to your advantage

        # Set left pointer to left side of array
        # Set right pointer to right side of the array
        leftPointer = 0
        rightPointer = len(numbers) - 1
        solutionFound = False
        solution = []

        # Add the two numbers at the pointer index together
        # If it is too big, decrease right pointer
        # If it is too small, increase left pointer 
        # If it is just right, return leftpointer + 1, rightpointer + 1

        while solutionFound == False:
            if (numbers[leftPointer] + numbers[rightPointer]) > target:
                rightPointer -= 1
            elif (numbers[leftPointer] + numbers[rightPointer]) < target:
                leftPointer += 1
            elif (numbers[leftPointer] + numbers[rightPointer]) == target:
                solutionFound = True
                solution = [leftPointer + 1, rightPointer + 1]

        return solution
            