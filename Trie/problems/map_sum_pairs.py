'''
https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1058/

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
'''

'''
Solution: I've used an extra map here because I didn't want to mess with Trie implementation. 

Otherwise, you could modify the Trie code to hold an integer (is_terminating will be True, when this integer is popualted).

you could modify serialize to return the sum of all integers stores in the nodes.
'''

# import Trie # copy Trie code here or import from one directory above

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_value = {}
        self.trie = Trie()

    def insert(self, key, val):
        self.word_value[key] = val
        self.trie.insert(key)

    def sum(self, prefix):
        return sum([self.word_value[w] for w in self.trie.list_words_with_prefix(prefix)])
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)