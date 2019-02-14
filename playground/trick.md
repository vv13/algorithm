## 模板
```
const executor = require('../executor');

const input = ['123456'];

function main() {}

executor(main, input);
```

## 把戏

#### 加法防溢出
```
a + (b - a) / 2
```

#### 不增加新变量交换数字
```
a = a ^ b
b = a ^ b
a = a ^ b
```
