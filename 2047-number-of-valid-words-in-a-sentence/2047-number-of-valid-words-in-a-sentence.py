# this was no-where close to easy tier

class Solution:
    def countValidWords(self, sentence: str) -> int:
        punc = "!.,"
        nums = "0123456789"
        split_sen = re.split(r'\s+', sentence.strip())
        count = 0

        for word in split_sen:
            if (not word): continue
            if (any(char in nums for char in word)): continue
            if (sum(char in punc for char in word) > 1): continue
            
            hyphen_count = word.count('-')
            if (hyphen_count > 1): continue
            if (hyphen_count == 1):
                hyphen_index = word.index('-')
                if (hyphen_index == 0 or hyphen_index == len(word) - 1): continue
                if (not (word[hyphen_index - 1].islower() and word[hyphen_index + 1].islower())): continue
            
            if (any(char in punc and char != word[-1] for char in word)): continue
            
            count += 1

        return count
