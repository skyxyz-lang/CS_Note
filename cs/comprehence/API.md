### 接口的幂等性
https://www.cnblogs.com/jajian/p/10926681.html
>维基百科上的定义：
幂等（idempotent、idempotence）是一个数学与计算机学概念，常见于抽象代数中。
在编程中一个幂等操作的特点是其任意多次执行所产生的影响均与一次执行的影响相同。

>幂等函数，或幂等方法，是指可以使用相同参数重复执行，并能获得相同结果的函数。
这些函数不会影响系统状态，也不用担心重复执行会对系统造成改变。
>例如，“setTrue()”函数就是一个幂等函数,无论多次执行，其结果都是一样的，更复杂的操作幂等保证是利用唯一交易号(流水号)实现.

考虑幂等性的场景
1. 前端重复提交
2. 接口超时重试
3. 消息重复消费

实现方式
1. Token机制
2. 数据库去重表
3. Redis实现
4. 状态机
