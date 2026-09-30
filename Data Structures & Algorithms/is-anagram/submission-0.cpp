class Solution {
public:
    bool isAnagram(string s, string t) {
        // Strings can be empty
        if (s.size() != t.size()) {
            return false;
        } else if (s.size() == 0 && t.size() != 0) {
            return false;
        } else if (s.size() != 0 && t.size() == 0) {
            return false;
        }

        // Bool found character. Default it to true
        bool found_character = true;

        // Create an i loop. Iterate through it until s.size()
        for (int i = 0; i < s.size(); i++) {
            // First, check if the bool found character is set to true.
            // If it is set to false then that specific s[i] character was not found in the
            // entire array, so break
            if (found_character == false)
                break;

            // Set found_character to false as a base case.
            // That way, we know for sure that the character has to be found within the 
            // t string, as it must be marked true.
            found_character = false;

            // Nest j loop. Iterate it until t.size()
            for (int j = 0; j < t.size(); j++) {
                // Check s[i] for each t[j]
                if (s[i] == t[j]) {
                    // If values are equal, set t[j] value to zero
                    t[j] = 0;
                    found_character = true;
                    break;
                }
            }
        }
        // Outside the for loop, return false if bool found character is false.
        // Else return true.
        return found_character;
    }
};
