Assume we have a function, receiving several parameter and do something:
```
function doSomething(task1, task2, task3) {
  task1()
  task2()
  task3()
}
```

Then we should implement a fn to make function Curry:
```
function curry() {}

const curried = curry(doSomething)

curried(task1, task2, task3)
curried(task1, task2)(task3)
curried(task1)(task2)(task3)
```
