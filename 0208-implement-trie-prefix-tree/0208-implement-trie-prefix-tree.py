class Trie:

    def __init__(self):
        self.res = []

    def insert(self, word: str) -> None:
        self.res.append(word)

    def search(self, word: str) -> bool:
        if(word in self.res): return True
        else : return False

    def startsWith(self, prefix: str) -> bool:
        ans = [p for p in self.res if p.startswith(prefix)]
        return True if(ans) else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)