'''
https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1057/

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''




'''
Solution:

For a number, xor value will be maximum with a number which is closest (lexicographically) to its bit inverse
ex: 00101, bit inverse is 11010, 11001 will produce a greater XOR value than 11100

For every number is the given array, we need to find another number in the array which is lexicographically closest to the current element's inverse.

1. construct a Trie with bit strings (normalized to 31 bits since elements are less than 2^31)
2. For each element's bit inverse find the element from the Trie which is lexicographically closest (most significant bits are the same)
'''


# import Trie # copy Trie code here or import from one directory above

def lexicographic_closest_match(trie, word):
    match = ''
    curr_node = trie.root
    for c in word:
        if c not in curr_node.children:
            c = '0' if c=='1' else '1'
        curr_node = curr_node.children.get(c)
        match = match + c
    return match

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
      bit_strings = ['{0:b}'.format(x).zfill(31) for x in nums]
      trie = Trie(bit_strings)
      inv_bit_strings = ['{0:b}'.format(2**31-1 - x).zfill(31) for x in nums]
      return max([nums[i] ^ int(lexicographic_closest_match(trie, inv_bit_strings[i]), 2) for i in range(len(nums))])