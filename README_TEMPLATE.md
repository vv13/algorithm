## leetcode
| 序号 | 名称 | 难度 | 标签 | 链接 | 备注 |
| :----:| :---- | :----: | :----: | :----: | :---- |
${leetcode}

## 开启你的刷题之旅
### 获取题目信息
选取你想要练习的题目编号，通过 [leetcode-problems-crawler](https://github.com/vv13/leetcode-problems-crawler) 进行题目信息爬取：
```
npx leetcode-problems-crawler  -l python3 -r 1
```

此时会在当前文件夹下生成如下目录：
```
001.two-sum.easy
├── README.md
└── solution.py
```

### 编写测试代码
我实现了一个比较简单的代码执行器，首先将文件 `leetcode/utility/test_runner.py` 复制到文件夹中，并创建 `test.py` 文件，此时的目录信息为：
```
001.two-sum.easy
├── README.md
└── solution.py
├── test_runner.py
├── test.py
```

打开 `test.py`，编写通用测试代码，并添加一个测试用例数据：
```

from test_runner import testRunner
from solution import Solution


if __name__ == "__main__":
    inputs = [
        [[2, 7, 11, 15], 9]
    ]
    expects = [[0, 1]] # 可不传此结果集，直接观察输出结果
    testRunner(inputs, Solution, expects)
```

没错，执行测试代码就是这么简单，`testRunner` 会自动解析所有类方法，并将 `inputs` 数组通过正确的形式进行传入，现在编写 `solution.py`，让我们来实现两种不同的解法：
```python
from typing import List

class Solution(object):
    # brute force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, cur in enumerate(nums):
            expect = target - cur
            if expect in map:
                return [map[expect], index]
            map[cur] = index

```

之后，直接执行 `test.py` 观察输出结果：
```
$ python test.py
twoSum :
result: [0, 1], passed
all test passed

twoSum1 :
result: [0, 1], passed
all test passed

```

若需要生成 README，请参考 `generate_markdown.py` 文件，欢迎 star 或 folk。

## 相关文章
- [冒泡、选择与插入排序](https://vv13.cn/Algorithm/%E5%86%92%E6%B3%A1%E3%80%81%E9%80%89%E6%8B%A9%E4%B8%8E%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F/)
- [求质数的几种方法](https://vv13.cn/Algorithm/%E6%B1%82%E8%B4%A8%E6%95%B0%E7%9A%84%E5%87%A0%E7%A7%8D%E6%96%B9%E6%B3%95/)
- [八皇后问题](https://vv13.cn/Algorithm/%E5%85%AB%E7%9A%87%E5%90%8E%E9%97%AE%E9%A2%98/)
- [汉诺塔问题](https://vv13.cn/Algorithm/%E6%B1%89%E8%AF%BA%E5%A1%94%E9%97%AE%E9%A2%98/)
