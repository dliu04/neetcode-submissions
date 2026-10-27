class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalList = []

        nums.sort()

        for i in range(len(nums)):
            # De-duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                result = nums[i] + nums[l] + nums[r]

                if result < 0: # too small
                    l += 1
                elif result > 0: # too big
                    r -= 1
                else: # result is 0
                    finalList.append([nums[i], nums[l], nums[r]])

                    # De-duplicate
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    # Iterate
                    l += 1
                    r -= 1

        return finalList