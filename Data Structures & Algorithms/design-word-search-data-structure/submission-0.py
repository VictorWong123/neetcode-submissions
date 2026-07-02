class TrieNode:
    def __init__(self):
        self.trie = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.trie:
                cur.trie[c] = TrieNode()
            cur = cur.trie[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j,len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.trie.values():
                        if dfs(i+1,child):
                            return True
                    return False
                    
                else:
                    if c not in curr.trie:
                        return False
                    curr = curr.trie[c] 

            return curr.word
        return dfs(0,self.root)






        
