from collections import deque


def word_ladder_II(begin_word, end_word, word_dict):
    """
    Find all transformation path from begin_word to end_word
    :param begin_word: 
    :param end_word: 
    :param word_dict:
    :type word_dict: set
    :return: 
    """

    word_dict.add(end_word)
    words_visited = set()
    words_to_visit = deque()
    words_graph = {}  # {word: [neighbor_word0, ...]}
    words_to_visit.append(begin_word)

    while words_to_visit:
        breadth = len(words_to_visit)
        for i in range(breadth):
            word = words_to_visit.popleft()
            if word in words_visited:
                continue
            words_visited.add(word)
            if word in word_dict:
                word_dict.remove(word)
            for j in range(len(word)):
                for k in range(26):
                    new_word = word[:j] + chr(ord('a') + k) + word[j + 1:]
                    if new_word in word_dict:
                        if words_graph.get(word, None):
                            words_graph[word].append(new_word)
                        else:
                            words_graph[word] = [new_word]
                        words_to_visit.append(new_word)
    word_ladders = []
    ladder = []
    depth_first_search(begin_word, end_word, words_graph, word_ladders, ladder)
    return word_ladders


def depth_first_search(word, end_word, words_graph, word_ladders, ladder):
    if word == end_word:
        ladder.append(word)
        if word_ladders:
            if len(ladder) < len(word_ladders[0]):
                word_ladders = [list(ladder)]
            elif len(ladder) == len(word_ladders[0]):
                word_ladders.append(list(ladder))
        else:
            word_ladders.append(list(ladder))
        return

    ladder.append(word)
    for n in words_graph.get(word, []):
        depth_first_search(n, end_word, words_graph, word_ladders, ladder)
        ladder.pop()


print(word_ladder_II("hit", "cog", {"hot", "dot", "dog", "lot", "log", "cog"}))
