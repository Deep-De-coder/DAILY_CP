class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # a=[]
        # ltos = ' '.join(map(str, words))
        # b=ltos.split()
        # for i in b:
        #     if i == separator:
        #         a=a.append(b[i])
        a=[]
        for i in words:
            w= i.split(separator)
            print(w)
            for i in w:
                if(i != ""):
                    a.append(i)
        return a
