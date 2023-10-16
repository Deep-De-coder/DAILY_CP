class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #Program 1
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
        


        # Program 2
        res = []
        for i in image:
            res.append([x ^ 1 for x in i[::-1]])
        return res
