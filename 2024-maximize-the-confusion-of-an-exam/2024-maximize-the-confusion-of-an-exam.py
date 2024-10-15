# now this was a good one 

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        anslist = list(answerKey)
        l, max_count, slide = 0, 0, 0

        c = Counter()

        for r in range(len(anslist)):

            c[anslist[r]] += 1
            max_count = max(max_count, c[anslist[r]])
            if (r - l + 1) - max_count > k:
                c[anslist[l]] -= 1
                l += 1

            slide = max(slide, r - l + 1)

        return slide

