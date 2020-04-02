修改下面的 start 函数, 使 execute 对应的 id 按顺序打印.
```

function start(id) {
  execute(id).catch(console.error);
}

// 测试代码 (请勿更改):

console.log('输出结果:');

for (let i = 0; i < 5; i++) {
  start(i);
}

function sleep(duration) {
  return new Promise(resolve => setTimeout(resolve, duration));
}

function execute(id) {
  let duration = Math.floor(Math.random() * 500);

  return sleep(duration).then(() => {
    console.log('id', id);
  });
}

// 输出结果参考
// id 0
// id 1
// id 2
// id 3
// id 4

```
