# <!-- 1st Approach Memory % is more -->
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return ' '.join(s)


# <!-- 2nd Approach Runtime % is More 96.68% -->
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s.split(' ')
#         new = ''
#         for word in s:
#             new += word[::-1] + ' '

#         return new[:-1]
