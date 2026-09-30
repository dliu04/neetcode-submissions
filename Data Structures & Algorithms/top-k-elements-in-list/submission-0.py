class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # A good question to ask:
        # Will the array always be automatically sorted?
        
        # I think you can just sort it by most to least
        # then just pick the unique elements k times and return
        
        # Dictionary where the key is the num and the value is the count?
        result = defaultdict(int)

        for num in nums:
            result[num] += 1
        
        resultArray = []

        for i in range(k):
            resultArray.append(max(result, key=result.get)) # Append key with max value
            # Remove it from array and move on to the next k element
            del result[max(result, key=result.get)]
        
        return resultArray
