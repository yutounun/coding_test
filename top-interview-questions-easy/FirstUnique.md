# problem
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

```
Input: s = "leetcode"
Output: 0
```
Example 2:

```
Input: s = "loveleetcode"
Output: 2
```
Example 3:

```
Input: s = "aabb"
Output: -1
```

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
# solution

```python
import string
class Solution:
    def firstUniqChar(self, s: str) -> int:
#         [a to z]
        letters  = string.ascii_lowercase
#     if a..z is unique in s, output index of a..z in s
        index=[s.index(l) for l in letters if s.count(l) == 1]
#     find the first non-repeating character is one of condition
        return min(index) if len(index) > 0 else -1
```