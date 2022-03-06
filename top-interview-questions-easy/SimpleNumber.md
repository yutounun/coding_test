# problem
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

```
Input: nums = [2,2,1]
Output: 1
```

Example 2:

```
Input: nums = [4,1,2,1,2]
Output: 4
```

Example 3:

```
Input: nums = [1]
Output: 1
```

Constraints:

```
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
```

# solutions
この方法の方が馴染みあるが、配列は順番を意識するしINDEXあるからメモリもスピードもよくない

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []
        
        for x in nums:
            if x in ans: 
                ans.remove(x)
            else: ans.append(x)
        
        return ans.pop()
```


set(集合)は並び順など関係ないので、O(n)となり、much faster than appending to a list.
INDEX番号とか順序関係ない問題だから、setの方が圧倒的に良い

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        S = set()
        
        for x in nums:
            if x in S: S.remove(x)
            else: S.add(x)
        
        # このときのSにはダブってない数値が一つだけ入ってる(1,)みたいに。
        # 順序がないから取得する方法はpopでよい
        return S.pop()
```