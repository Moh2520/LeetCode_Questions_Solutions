class Solution:
    def stringMatching(self, words):
        words = sorted(words, key=len)
        res = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res