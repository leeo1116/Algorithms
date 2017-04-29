class TrieNode(object):
    def __init__(self):
        self.is_word = False  # Initially there is no children, it's empty
        self.children = {}  # Use dictionary to make accessing children fast


def string_in_dict(d, s):
    """
    Given a dictionary containing multiple strings, check if a given string exists in it.
    Note: s may contain '*' which can represent any character
    :param d: dictionary contains strings
    :param s: given string
    :return: if s exists in d
    """
    root = TrieNode()
    for w in d:
        trie_insert(root, w)
    return trie_search_wildcard_recursive(root, s)


def trie_insert(root, w):
    """
    Insert a word into a trie
    :param root: root of the trie
    :type root: TrieNode
    :param w: word to be inserted
    :type w: str
    :return: None
    """
    r = root
    for c in w:
        r.children[c] = TrieNode()
        r = r.children[c]


def trie_search(root, w):
    """
    Search a word in trie
    :param root: root of the trie
    :type root: TrieNode
    :param w: target word
    :type w: str
    :return: if w can be found in trie
    :rtype: bool
    """
    r = root
    for c in w:
        if r.children.get(c, None) is None:
            return False
        else:
            r = r.children[c]
    return r.children == {}


def trie_search_wildcard_recursive(root, w):
    """
    Search in Trie with wildcard, recursively
    :param root:
    :type root: TrieNode
    :param w: 
    :return: 
    """
    if root.children == {} and w == "":
        return True

    for i, c in enumerate(w):
        if c == '*':
            for child in root.children.values():
                if trie_search_wildcard_recursive(child, w[i + 1:]):
                    return True
        else:
            if root.children.get(c, None) is None:
                return False
            else:
                return trie_search_wildcard_recursive(root.children[c], w[i + 1:])
    return False


def trie_search_wildcard_iterative(root, w):
    """
    Search in Trie with wildcard, iteratively
    :type root: TrieNode 
    :type w: str 
    :rtype: bool
    """
    # r = root
    # for c in w:
    #     if c == '*':
    #         children_tmp = r.children
    #     else:
    #         children_tmp = {c: r.children[c]}
    #     r_tmp = r
    #     for child in children_tmp.items():
    #         r_tmp = child
    # How to proceed? Iteration will be difficult if not impossible
    # Because it's difficult to know how many '*'s will be there

print(string_in_dict({"abc", "kst", "opr"}, "**"))
