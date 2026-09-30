class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force: For each index i, iterate through and multiply by the product of all elements
        # except for i and store
        # Runtime complexity: O(n^2)
        result = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue # Restart the loop and increment
                else:
                    product *= nums[j]
            result.append(product)
        return result

    # Maybe there is a way to "store" products we have already seen before so we don't have
    # to calculate it every single time?
    
    # But, what useful data structure can store these values? And how would we retrieve them?
    # Eggsample: nums = [1,2,4,6]
    # 2 times 4. I have not seen 2 times 4. Proceed with operation.
