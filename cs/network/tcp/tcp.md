### 什么时候出现 time_wait 和 close_wait
> 对于TCP关闭连接的过程中，主动发起连接关闭的一方会进入time_wait状态，被动的一方会进入close_wait状态
### time_wait的意义 2msl
1. 确保对方收到自己发送的最后一个ack，如果没有收到，那么对方必然发送FIN
2. 便面上一个连接的包影响下一个建立的连接，利用最长的2msl，让残余的IP报文在网络中消失

### 出现大量close_wait 和time_wait的分别的原因是什么以及解决办法
TCP_TIMEWAIT_LEN

1. 大量close_wait
    1. 应用程序写的有问题，没有正确的关闭socket
    2. CPU没有调度到应该程序，或者应用程序阻塞在其他地方，导致应用程序一直没有执行close操作

2. 大量 time_wait原因
    1. 作为客户端有大量的连接过来，然后关闭了之后由于有 2msl的时间限制，所以导致了有大量的 time_wait
    2. RFC 795 建议的msl=2分钟，linux实践中msl=30秒
    3. 一般负载均衡服务器或者反向代理服务器会有此问题
3. time_wait的危害
    1. 占用连接资源，新的连接不能创建
    2. 占用内存资源，可忽略
4. 解决办法
```bash
开启time_wait状态端口的重用，允许其用于新的tcp连接
net.ipv4.tcp_tw_reuse = 1 <br/>
开启TCP连接中的time_wait状态 的sockets的sockets的快速回收，系统会保存最近一次该socket连接上的传输报文（包括数据或者仅仅是ACK报文）的时间戳，当相同四元组socket过来的报文的时间戳小于缓存下来的时间戳则丢弃该数据包，并回收这个socket。
但是会导致NAT网络下丢包
net.ipv4.tcp_tw_recycle = 1
# 修改FIN_WAIT-2时间的时长，默认是60s
net.ipv4.tcp_fin_timeout = 60
# 用于外连使用的随机高位端口范围, 决定了可以建立多少个链接
net.ipv4.ip_local_port_range = 32768 60999
# 开启时间戳，上面两个功能依赖于此
net.ipv4.tcp_timestamps
```

### 参考文档：
1. https://www.cnblogs.com/rexcheny/p/11143128.html
2. https://juejin.cn/post/6844903730874171405
3. https://zhuanlan.zhihu.com/p/40013724