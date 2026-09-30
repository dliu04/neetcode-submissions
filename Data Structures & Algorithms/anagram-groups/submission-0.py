class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For each string inside this list:
            # Compare it with the first string in a bucket
                # If it is an anagram, place the string in the bucket
                # Else if no compatible bucket is available, create one and 
                # place the current string in it.
        # Return the main list with its sublists (buckets).


        # Okay so that didn't really work out. We should try a different approach.
        # Create a dictionary of lists
        # A dictionary is associated with a key, value pair. 
        # The key can be a NORMALIZED string. Sorted alphabetically
        # If the key equals the normalized string, include it in the dictionary's value
        # Else create a new dictionary entry with a new list
        # Include all dictionary values into a big list. Return big list 

        mainList = list()
        stringDictionary = {}

        for string in strs:
            if len(stringDictionary) == 0:
                stringDictionary[''.join(sorted(string))] = [string] # Add to dict with normalized string as key
                continue
            if ''.join(sorted(string)) in stringDictionary: # If the normalized key already exists
                stringDictionary[''.join(sorted(string))].append(string) # append string to list
            else:
                stringDictionary[''.join(sorted(string))] = [string] # create new list

        # Make a new main list with sublists
        # (List the lists of the dictionary)
        mainList = list(stringDictionary.values())

        return mainList
        ## After viewing the hint
        # By definition of an anagram, we only care about the frequency
        # of each character in a string. 
        # We can use an array of O(26) (to represent the alphabet) that stores
        # the frequencies of each character in a given string.
        # Then, we can use this array as a key to gather up other strings that share
        # this key to put into a sublist.

    def isAnagram(self, string1, string2):
        sorted1 = ''.join(sorted(string1))
        sorted2 = ''.join(sorted(string2))
        
        if sorted1 == sorted2:
            return True
        else:
            return False

        