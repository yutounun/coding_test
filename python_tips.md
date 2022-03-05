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

# ソート
```python
newA = sorted(A)
```
Does not change original array, so you have to use a new varible.

```python
newB = sorted(B, reverse=True)
```

# 絶対値
```python
print(abs(-2))
# -2
```

# 配列のINDEXを取得
```python
for idx, val in enumerate(arr):
```

# for, range
rangeを使うときに範囲を指定するなら終了値は+1しないといけない

```python
# 1~100まで出力する場合
for i in range(1,101)
```