# Sol 1
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s_backspaced = []
#         t_backspaced = []
        
#         for i in range(len(s)):
#             if s[i] == '#':
#                 if s_backspaced:
#                     s_backspaced.pop()
#             else:
#                 s_backspaced.append(s[i])
            
#         for i in range(len(t)):
#             if t[i] == '#':
#                 if t_backspaced:
#                     t_backspaced.pop()
#             else:
#                 t_backspaced.append(t[i])
        
#         return s_backspaced == t_backspaced

# Sol 2
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def backwardResult(string):
#             debt = 0
            
#             for c in reversed(string):
#                 if c == '#':
#                     debt += 1
                
#                 elif debt > 0:
#                     debt -= 1
                
#                 else:
#                     yield c
        
#         return all(a == b for (a, b) in zip_longest(backwardResult(s), backwardResult(t)))

# Sol 3
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
    	a, A = [collections.deque(), collections.deque()], [S,T]
    	for i in range(2):
	    	for j in A[i]:
   		 		if j != '#': a[i].append(j)
   		 		elif a[i]: a[i].pop()
    	return a[0] == a[1]
		
		
		
