class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a set
        # For each number:
            # Check if the number already exists in the set: if yes, return false
            # Add the number into the set

        # return true

        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)


        return False