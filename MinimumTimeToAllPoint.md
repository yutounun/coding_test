

# solution
```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sec = 0
        x1,y1 = points.pop()
        while points:
            x2,y2 = points.pop()
            sec += max(abs(x2-x1),abs(y2-y1))
            x1,y1 = x2,y2
        return sec
```

- popは配列の後ろの一個取得して、元の配列から削除する
- x2,y2はx1,y1になって一つ前の配列がx2,y2になる
- [[1,2],[2,5]]の場合、差がより大きい方(xかyのうち)の差分を足して行ってそれが答えになる

# ref
https://qiita.com/KueharX/items/7949b94ac52e1b81147c