Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
```

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

Constraints:

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lower-case English letters.


```python
class Solution(object):
   def longestCommonPrefix(self, strs):
      """
      :type strs: List[str]
      :rtype: str
      """
      # 入力配列が空なら空return
      if len(strs) == 0:
         return ""
      # strs配列の最初の単語をcurrentに
      current = strs[0]
      # strs配列の２番目の単語以降と最初の単語を比べていく
      for i in range(1,len(strs)):
          temp = ""
          #  ２番目以降の単語の一文字ずつチェック
          for j in range(len(strs[i])):
              # １番目の一文字目と２番目の１番目が同じならtempにその文字を追加
              if j<len(current) and current[j] == strs[i][j]:
                  temp+=current[j]
              else:
                  break
          # ２単語目の一文字ずつチェック終わったらcurrentをチェックしたところまで更新する
          current = temp
      return current
```