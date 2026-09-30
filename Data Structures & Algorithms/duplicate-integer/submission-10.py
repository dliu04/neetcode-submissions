class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Insantiate a set data structure 

        for num in nums: # for each number in the list
            if num in seen: # Checks if the value exists in sequence (seen)
                return True
            seen.add(num) # If not, add number into the seen set
        
        return False # if the loop ends, then return false