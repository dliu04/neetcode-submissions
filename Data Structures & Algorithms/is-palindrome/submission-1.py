class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Reverse the string
        # Compare the two strings

        # Pretty sure even number strings can also be palindromes.
        # wasitacaroracati???saw is a palindrome? Cuz ignores non alphanumeric characters

        # Have a pointer at the start and at the end of a string
        # Compare each character, each pointer going towards the middle
        # on each iteration


        # Remove non-alphanumeric characters
        cleaned_string = ''.join(char for char in s if char.isalnum()).lower()
        front_pointer = 0
        back_pointer = len(cleaned_string) - 1

        # If it is an odd number string, and if the two halves are equal up until the middle
        # character, then the while loop won't run (front pointer < back pointer) 
        # and it is a confirmed palindrome.

        # This while loop will also still run if it is an even number string.
        while front_pointer < back_pointer:
            if cleaned_string[front_pointer] != cleaned_string[back_pointer]:
                return False
            front_pointer += 1
            back_pointer -= 1
        
        return True
