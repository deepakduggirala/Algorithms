class TrieNode():
    def __init__(self, is_terminating=False):
        self.is_terminating = is_terminating
        self.children = {}

class Trie():
    # Trie for only Strings
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
            
    def insert(self, word):
        # inserts the given word into Trie
        curr_node, rem = self.explore(word)
        for s in rem:
            curr_node.children[s] = TrieNode()
            curr_node = curr_node.children.get(s)
        curr_node.is_terminating = True
    
    def explore(self, string):
        # internal method
        # explore:: String -> (TrieNode, String)
        # explore traverses down the Trie one character at a time, until it cannot go anymore either because the string is exhausted or a required node is not present, and returns the last node and the remaining string.
        curr_node = self.root
        for i,s in enumerate(string):
            if s in curr_node.children:
                curr_node = curr_node.children.get(s)
            else:
                return (curr_node, string[i:])
        return (curr_node, [])
    
    def serialize(self, node):
        # internal method
        # return a list of words (terminating is True) starting from the given node
        words = []
        for c, c_node in node.children.items():
            if c_node.is_terminating:
                words.append(c)
            for s in self.serialize(c_node):
                words.append(c+s)
        return words
            
    def search(self, string):
        # returns true if the word is in Trie (terminating should be true)
        curr_node, rem = self.explore(string)
        return len(rem) == 0 and curr_node.is_terminating
    
    def starts_with(self, prefix):
        # returns true if the prefix is in Trie (terminating may or may not be true)
        curr_node, rem = self.explore(prefix)
        return len(rem) == 0
    
    def list_words_with_prefix(self, prefix):
        # returns all words (terminating is True) that start with given prefix
        curr_node, rem = self.explore(prefix)
        if len(rem) != 0:
            return []
        words = [prefix+s for s in self.serialize(curr_node)]
        if curr_node.is_terminating:
            return [prefix] + words
        else:
            return words