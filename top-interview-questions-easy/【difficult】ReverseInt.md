# problem
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

# solution
```python
class Solution:
    # @return an integer
    def reverse(self, x):
        negFlag = 1
        if x < 0:
            negFlag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1])
        
        return 0 if x > pow(2, 31) else x * negFlag
```