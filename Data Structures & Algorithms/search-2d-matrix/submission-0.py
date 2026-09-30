class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First, check if the target is within range
        # of the left and right side of the middle row 
        # if not, go to a different row accordingly

        leftRow = 0
        rightRow = len(matrix) - 1

        while leftRow <= rightRow:
            # First, locate the middle row index
            middleRow = (leftRow + rightRow) // 2

            # Then, check if the target is within the range of
            # that specific row
            leftPointer = 0
            rightPointer = len(matrix[middleRow]) - 1

            # If the target is within that row, perform a basic binary search
            # If not, change the search area accordingly
            if target < matrix[middleRow][leftPointer]:
                rightRow = middleRow - 1
            elif target > matrix[middleRow][rightPointer]:
                leftRow = middleRow + 1
            else: # The target is feasible in the row, perform basic binary search
                while leftPointer <= rightPointer:
                    middle = (leftPointer + rightPointer) // 2
                    if target < matrix[middleRow][middle]:
                        rightPointer = middle - 1
                    elif target > matrix[middleRow][middle]:
                        leftPointer = middle + 1
                    else: # it equals
                        return True

                # Basic binary search failed, target isn't in valid row
                return False

        # If you exit loop, return false
        return False
