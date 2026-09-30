class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Maybe there is a way to "store" products we have already seen before so we don't have
        # to calculate it every single time?

        # How do we iterate through the array, get all the products only once?
        result = []
        product = 1
        containsZero = False
        containsZeroIndex = 0
        containsTwoZeroes = False

        for i in range(len(nums)):
            if nums[i] == 0 and containsZero == True:
                containsTwoZeroes = True
                break
            if nums[i] == 0:
                containsZero = True
                containsZeroIndex = i
                continue
            product *= nums[i]
        
        for i in range(len(nums)):
            if containsZero == True and containsTwoZeroes == False:
                # Populate the array with zeroes except for the index that it contains in
                result = [0] * len(nums)
                result[containsZeroIndex] = product
            elif containsTwoZeroes == True:
                result = [0] * len(nums)
            else:
                result.append(int(product / nums[i]))
        
        return result 
    
        # But, what useful data structure can store these values? And how would we retrieve them?
        # Eggsample: nums = [1,2,4,6]
        # Starting on index 1
        # 2 times 4. I have not seen 2 times 4. Proceed with operation.
