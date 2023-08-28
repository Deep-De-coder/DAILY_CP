class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

'''
Intuition
If we can find the length of the needle then we can use that as the window size and use the sliding windows approach to solve this problem

Approach
This is a Python function that implements the "strstr" function, which searches for a substring within a larger string. The function takes two string arguments, haystack and needle, and returns the index of the first occurrence of the needle in the haystack, or -1 if the needle is not found.

Here's a step-by-step explanation of how the code works:

The function starts by checking if needle is equal to haystack. If it is, then needle is a substring of haystack and its starting index is 0. In this case, the function returns 0.

If needle is not equal to haystack, the function initializes two variables: i, which represents the starting index of a substring of haystack, and j, which represents the ending index of that substring. Initially, i is set to 0 and j is set to the length of needle.

The function then enters a loop that continues until j is greater than the length of haystack. In each iteration of the loop, the function extracts a substring of haystack that starts at index i and ends at index j - 1. This substring is stored in a variable called currentNeedle.

The function then compares currentNeedle with needle. If they are equal, it means that needle is a substring of haystack starting at index i. The function returns i.

If currentNeedle is not equal to needle, the function increments i and j by 1 and continues with the next iteration of the loop.

If the loop completes without finding a match for needle, the function returns -1.

Overall, this function provides a simple and efficient way to search for substrings within a larger string in Python.

Complexity
Time complexity:
O(mn)

Space complexity:
O(n)

The time complexity of this function is O(mn), where m is the length of haystack and n is the length of needle. This is because in the worst case scenario, we need to compare every substring of haystack of length n with needle.

The space complexity of this function is O(n), because we are using a slicing operation haystack[i:j] which return a copy of substring, Which can be of size n.

Code
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        i = 0
        j = len(needle)
        while j <= len(haystack):
            currentNeedle = haystack[i:j]
            if currentNeedle == needle:
                return i
            i += 1
            j += 1
        return -1
  '''
