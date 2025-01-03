class Solution:
    def vowelStrings(self, words, queries):
        vowels = {"a", "e", "i", "o", "u"}
        
        # Step 1: Create a prefix sum array
        prefix = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            first = word[0]
            last = word[-1]
            # Check if the word is a "vowel string"
            if first in vowels and last in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        
        # Step 2: Answer each query in O(1)
        result = []
        for l, r in queries:
            count = prefix[r + 1] - prefix[l]
            result.append(count)
        
        return result
        # # print(words[0:3])

        # v = set(["a", "e", "i", "o", "u",])

        # # l, r = queries[0]
        # # print(l,r)

        # res = []

        # for q in queries:
        #     l, r = q
        #     count = 0
        #     for i in range(l,r+1):
        #         first = words[i][0]
        #         last = words[i][-1]
        #         if first in v and first == last:
        #             print(f"Yes in string: {words[i]}, first vowel is: {first} and last vowel is: {last}")
        #             count+=1
        #         else:
        #             print(f"This words is WEIRD: {words[i]}")
        #     res.append(count)
        # return res
if __name__=="__main__":
    words = ["aba","bcb","ece","aa","e"]
    queries = [[0,2],[1,4],[1,1]]

