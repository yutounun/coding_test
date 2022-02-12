Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

 

Example 1:
```
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
```
Example 2:

```
Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
```
Example 3:

```
Input: nums = [1], index = [0]
Output: [1]
```

Constraints:
```
1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i
```

# solution1 slower

```python
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        # both len(nums) and len(index) are ok
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
# Runtime: 36 ms, faster than 36.25% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.
```
# solution2 faster
```python
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, v in zip(index, nums):
            res.insert(i, v)
        return res
# Runtime: 28 ms, faster than 90.08% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.
```

# tips
With insert function you can specify where to insert value.
With append function the values are added at the last of array.

## zip fucntion
- forループで複数のリストの要素を取得
- 要素数が異なる場合の処理
- zip()関数では多い分の要素が無視される
- itertools.zip_longest()関数では足りない分の要素が埋められる
- 複数のイテラブルの要素をタプルにまとめたリストを取得