'''
Here's how the code works:

The code initializesdto keep track of the count of each word or its reverse.

We iterate over each word inwords, and we use the lexicographic minimum of the word and its reverse (word[::-1])as the key for loading words into d, which ensures that the same pair is counted only once.

We return the sum of the counts of pairs in each value (usingx*(x-1)//2) as the answer.
'''

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        d = defaultdict(int)

        for word in words:
            d[min(word, word[::-1])]+= 1
        
        return  sum(map((lambda x: x*(x-1)), d.values()))//2
