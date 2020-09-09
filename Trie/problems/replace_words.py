'''
https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1053/

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
Example 3:

Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output: "a a a a a a a a bbb baba a"
Example 4:

Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 5:

Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
Output: "it is ab that this solution is ac"
'''

'''
Solution:

for each word, check in Trie if there is a terminating prefix for it, else return the word as is.
'''

# import Trie # copy Trie code here or import from one directory above

def f(word, t):
    curr_node = t.root
    prefix = ''
    for c in word:
        if c in curr_node.children:
            curr_node = curr_node.children.get(c)
            prefix = prefix + c
            if curr_node.is_terminating:
                return prefix
        else:
            return word
    return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
      trie = Trie(dictionary)
      return ' '.join(map(lambda w: f(w, trie), sentence.split(' ')))