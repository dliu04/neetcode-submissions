class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # [value, index]
        map = defaultdict(int) # Create new entry if entry doesn't exist

        for i in range(len(numbers)):
            # Calc the difference
            difference = target - numbers[i]
            if difference in map:
                # Return the indices
                return [map[difference] + 1, i + 1]

            # Else store num in map
            map[numbers[i]] = i
            