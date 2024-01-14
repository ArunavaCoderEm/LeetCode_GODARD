## NOT THE PROPER SOLUTION I GUESS AS IT DOESN'T CHECK THE OPERATIONS BUT WORKS

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if (len(word1) != len(word2)):
            return False
        else:
            count1 = Counter(word1) #dict word1 letter:occurance
            count2 = Counter(word2) #dict word2 letter:occurance
            w1 = sorted(count1.values()) ## occurance of each letter in word1
            w2 = sorted(count2.values()) ## occurance of each letter in woord2
            k1 = count1.keys() # letters in word1
            k2 = count2.keys() # letters in word2
            resC = (set(k1) == set(k2)) ## GIVES TRUE OR FALSE checking the letters 
            return (w1 == w2 and resC) # occurance and letters bothe true or not