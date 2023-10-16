class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for im in image:
            img = im[::-1]

            invert = []
            for i in img:
                if i == 1:
                    invert.append(0)
                else:
                    invert.append(1)
            ans.append(invert)
        return ans
        
