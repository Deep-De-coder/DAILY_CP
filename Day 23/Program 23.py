class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # stripp=s.strip()
        # dt=stripp.split(" ")
        # last=dt[-1]
        # return len(last)
        s = s.split()
        return len(s[-1])
'''
Approach
First we will convert given String of words into array of strings on basis of white spaces using python's .split() which converts the string into Array

for example:

str = "Hello World"
arr = str.split()

# arr will be
arr = ["Hello" , "World"]
So we will just return the length of last string from the array
Code
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[-1])

'''
