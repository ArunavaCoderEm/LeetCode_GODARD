class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        c1,c2 = Counter(list(secret)),Counter(list(guess))
        for i in range(len(guess)):
            if(secret[i] == guess[i]):
                bulls += 1
        cows = len(secret) - sum((c1 - c2).values()) - bulls
        return (f"{bulls}A{cows}B") 