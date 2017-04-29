class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        # build trie
        r = self.root
        for w in word:
            if r.children.get(w, None) is None:
                r.children[w] = TrieNode()
            r = r.children[w]
        r.is_word = True

    def search(self, word):
        return self.search_recursive(self.root, word)

    def search_recursive(self, root, word):
        if not word:
            return root.is_word
        r = root
        for i, w in enumerate(word):
            if r.children == {}:
                return False
            if w == '.':
                for c in r.children:
                    if self.search_recursive(r.children[c], word[i + 1:]):
                        return True
                return False
            else:
                if r.children.get(w, None):
                    r = r.children[w]
                else:
                    return False
        return r.is_word


d = WordDictionary()
d.add_word("li")
d.add_word("little")
print(d.search("..tl."))

