#### 操作系统的IO
>朴素方式，每次都在用户态进行判断文件描述符是否准备好
```python
fds = []
while True:
    # 所有文件描述符号
    for fd in fds:
        # 文件描述符ready，则处理数据
        if fd is ready:
            prcess(fd)

```
> select 方式
```C
while(1) {
    FD_ZERO(&reset);
    for(int i = 0l i< n l i++) {
        # reset 为位图大小1024
        FD_SET(fds[i], &reset);
    }
    # 用户态拷贝到内核态，并且阻塞直到有数据，并且修改位图的标记
    select(max+1, &reset, null, null, null);
    for(int i = 0; i< n l i++) {
        // 读处理
    }
}
```
缺点：
1. 1024 bitmap
2. rset 不可重用
3. 用户态拷贝到内核态开销
4. O(n)复杂度遍历

>poll
```C
struct pollfd {
    int fd;
    short events; //  监听什么事件、读、写
    short revents; // 读写数据来了进行置位
}
# 有数据都是置位、返回
# 轮训过程和select类似，只不过没有 1024的小时，以及避免不可重用的问题。

```

>epoll

```C
# 创建一个数据结构 epfd 内核态和用户态共享， 用户存储即将到来的事件
epfd = epoll_create(10)
# 增加文件描述符
epoll_ctr()

水平触发, nfds 有数据的个数
nfds = epoll_wait(xxx)
有数据：置位(重拍)

epoll 水平触发和边缘触发
水平触发：当被监听的文件描述符有可读写事件的时候，应用程序没有处理完成，那么下一次还是会重新通知。
边缘触发：当被监听的文件描述符有可读写事件的时候，应用程序没有处理完成，下次不会重新通知，直到该文件描述符有新的读写事件。
```