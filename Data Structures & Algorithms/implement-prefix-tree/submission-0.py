class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie

        for c in word:
            if c not in trie:
                trie[c] = {}

            trie = trie[c]

        trie['.'] = '.'


    def search(self, word: str) -> bool:
        trie = self.trie

        for i in word:
            if i not in trie:
                return False
            trie = trie[i]

        return '.' in trie
        

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie

        for i in prefix:
            if i not in trie:
                return False
            trie = trie[i]  

        return True
        
        
        