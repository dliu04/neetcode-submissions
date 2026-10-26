class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a-z 26
        # mapping character count of each string
        result = defaultdict(list) # new values are automatically added

        for s in strs:
            count = [0] * 26 # empty array of 26 0's

            for char in s:
                count[ord(char) - ord("a")] += 1

            # count is a list and cannot be a key
            # so change it into a tuple
            result[tuple(count)].append(s)
        
        return list(result.values())