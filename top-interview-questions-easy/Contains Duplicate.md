# solutions
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # print(len(nums),nums,len(set(nums)),len(nums))
        # 4 [1, 2, 3, 1] 3 {1, 2, 3}
        # ※ set does not include duplicated num
        return len(nums) != len(set(nums))
```