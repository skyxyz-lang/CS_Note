### python 相关相关基础知识

#### 装饰器
作用：增强函数的功能
原理：函数是对象、是变量,可以作为参数，可以作为返回值
使用场景：插入日志、性能测试、事务处理、缓存、权限校验等场景
```python
import time
def use_logging(func):
    """
    :param func:
    :return:
    """
    def wap(*args, **kwargs):
        st_time = time.time()
        res = func(*args, **kwargs)
        ed_time = time.time()
        print func.__name__ + 'is execute %ss' % str(ed_time - st_time)
        return res
    return wap


@use_logging
def add(a, b):
    print a + b
    return a + b

```