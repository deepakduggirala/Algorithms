'''
https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1056/
'''

'''
Backtracking and using Trie to stop early
'''

# import Trie # copy Trie code here or import from one directory above

def is_valid(p, m, n, visited):
    i,j = p
    return i >=0 and i < m and j >= 0 and j < n and (not visited[i][j])

def adjacent_letters(i, j, m, n, visited):
    left = (i, j-1)
    top = (i-1, j)
    right = (i, j+1)
    down = (i+1, j)
    res = [p for p in [left, top, right, down] if is_valid(p, m, n, visited)]
#     print(i,j,res)
    return res

def backtarck(p, root, m, n, board, visited):
    i,j = p
    c = board[i][j]
    
    if c in root.children:
        visited[i][j] = True
        word_lists = [is_in_trie(adj_p, root.children.get(c), m, n, board, visited) for adj_p in adjacent_letters(i, j, m, n, visited)]
        words = [word for sublist in word_lists for word in sublist]
        if root.children.get(c).is_terminating:
            words.append('')
        visited[i][j] = False
        return [c+w for w in words]
    else:
        return []

def findWords(board, words):
    trie = Trie(words)
    
    m = len(board)
    if m == 0:
        return []
    n = len(board[0])
    if n==0:
        return []

    found = []
    
    for b_i in range(m):
        for b_j in range(n):
            visited = [[False for c in range(n)] for r in range(m)]
            for x in backtarck((b_i,b_j), trie.root, m, n, board, visited):
                found.append(x)
    return list(set(found))
