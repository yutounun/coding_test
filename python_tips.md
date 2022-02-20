# 挿入
## append
リストの末尾に追加
```python
arr.append(1)
```
## insert
index指定で配列に追加できる

```python
A.insert(0,A[-1])
```
先頭に最後の要素を移動するケース

# カウント

## count
```python
arr.count(1)
```
でarrayの中に1が何個入っているかわかる

# 切り上げ・切り捨て
## math.floor
```python
import math

def solution(X, Y, D):
    return math.floor((Y - X) / D)
```
切り捨てする。
mathはimportする
## math.ceil
```python
import math

def solution(X, Y, D):
    return math.ceil((Y - X) / D)
```

切り上げする。
mathはimportする