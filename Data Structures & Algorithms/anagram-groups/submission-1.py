class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # DefaultDict automatically creates a key if the specified key was not found.
        # The value the key will associate itself with will be of type LIST.
        result = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                # Ord is a function that returns the unicode value of something.
                # This count list will now act as a specific pattern key.
                count[ord(char) - ord("a")] += 1
            # Lists are mutable, but tuples are immutable. Turn the key list into a key tuple.
            result[tuple(count)].append(string)

        return list(result.values())