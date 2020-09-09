'''
a word in give array can be

1. p (a palindrom)
  other words should be in these formats to make a new palindrom when combined
  - p
  - p2p (p2 is another palindrom)
2. x (not a palindrom)
  other words should be in these formats to make a new palindrom when combined
  - x1, px1 (x1 is x reversed)
3. px (starts with a palindrom)
  other words should be in these formats to make a new palindrom when combined
  - x1p,  p2x1p
4. xp (ends with a palindrom)
  other words should be in these formats to make a new palindrom when combined
  - x1, px1, p2px1

'''


# import Trie # copy Trie code here or import from one directory above

def is_palindrome(word):
    return word == word[::-1]

def palindromePairs(words):
    result = set()
    trie = Trie([w[::-1] for w in words])
    prefix_trie = Trie(words)
    index_map = {}
    for i,w in enumerate(words):
        index_map[w] = i
    for i,w in enumerate(words):
        if w == '':
            continue
        # words which are palindromes gets returned - done
        # will be nice if the position is also returned - done
        # what happens when there is an empty string in words? - add a pair of (p, e), (e, p) for every palindrome in words
        # w is in form of xp where x is non-palindrome string and p is a palindrome, then we need to search for x in Trie
        potential_palindromes = trie.list_words_with_prefix(w)
        for pot_pal in potential_palindromes:
            if is_palindrome(pot_pal[len(w):]):
                j = index_map[pot_pal[::-1]]
                if i!=j:
                    result.add((i,j))
                else:
                    # w is a palindrome
                    if '' in index_map:
                        e = index_map['']
                        result.add((i, e))
                        result.add((e, i))
                        
    for i,w in enumerate(words):
        if w == '':
            continue
        # find words that start with reverse of cuurent word
        for pot_pal in prefix_trie.list_words_with_prefix(w[::-1]):
            # if the rest of pot_pal (xrp) is also palindrome then new palindrome can be formed as xrpx
            # xr is reversed x
            if is_palindrome(pot_pal[len(w):]):
                j = index_map[pot_pal]
                if i!=j:
                    print(words[j], words[i])
                    result.add((j,i))
    return [[x,y] for x,y in result]
    
# words = ["abcd","dcba","lls","s","sssll"] #[[0, 1], [1, 0], [2, 4], [3, 2]]
words = ["a","b","c","ab","ac","aa"] # [[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]
palindromePairs(words)