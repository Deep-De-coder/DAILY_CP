class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]: 
        a, c, b =  defaultdict(int), [], items1 + items2
        for j in b:
            if j[0] not in a:  a[j[0]] = j[1]
            else: a[j[0]] = a[j[0]] + j[1]
        for i in sorted(a): c.append([i,a[i]])
        return c
