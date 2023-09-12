class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        se=set(nums)
        mis=[]
        for i in range (1,len(nums)+1):
            if i not in se:
                mis.append(i)
        return mis
        
