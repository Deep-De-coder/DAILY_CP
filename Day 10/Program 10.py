class Solution:
    def longestPalindrome(self, s: str) -> str:
         def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            palindrome1 = expandAroundCenter(i, i)
            # Even length palindrome
            palindrome2 = expandAroundCenter(i, i + 1)

            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest


'''Intuition: Expanding Around Centers
The idea behind this approach is to consider every character in the string as a potential center of a palindrome and then expand around that center to find the longest palindromic substring.

There are two cases to consider for the center:

One where the palindrome has an odd length (centered at a single character)
Image 002.png

Other where the palindrome has an even length (centered between two characters).
Image 001.png

By considering both cases, the algorithm effectively explores all possible palindromic substrings.

Approach
The expandAroundCenter function is defined within the main function. This helper function takes two parameters, left and right, which represent the potential center indices of the palindrome being expanded. It tries to expand the palindrome by moving left to the left and right to the right while the characters at these indices are the same.

The main function initializes an empty string longest to keep track of the longest palindromic substring found so far.

It iterates through the characters of the input string s using a for loop. For each character at index i, it considers two possible cases for the center of the palindrome:

Odd-length palindrome: The center is the character at index i.
Even-length palindrome: The center is between the characters at indices i and i + 1.

For each center, the expandAroundCenter function is called to find the longest palindromic substring that can be formed by expanding from that center.

The lengths of the obtained palindromic substrings (palindrome1 and palindrome2) are compared with the length of the current longest palindromic substring. If the length of a newly found palindrome is greater, the longest is updated with that palindrome.

Finally, the function returns the longest palindromic substring.

Complexity
Time complexity:
The main loop runs for each character in the string, and for each character, the expandAroundCenter function takes linear time to expand the palindrome. Hence, the total time complexity is O(N^2), where N is the length of the input string.

Space complexity:
The space complexity is O(1) as no additional data structures are used that grow with the input size.'''
