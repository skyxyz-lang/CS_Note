#### SDS (Simple Dynamic String)
应用：Redis 底层实现都是sds，是可以修改的字符串。
限制：小于1M，扩容加倍，大于1M,扩容增加1M，最高512M。
sds定义
```C
struct sdshdr {
    int len
    int free
    char buf[]
}
```
特性：
1. 二进制安全，（输入任何字节都能处理，包含零值字节，C的字符串对（\0）认为是字符串的结束）
2. 可以动态扩展
3. 兼容C字符串

#### Redis支持的数据结构
1. string   字符串  get(key) set(key, value) del(key)
2. list     列表  
3. set      集合  [SADD set_key value] [SMEMBERS set_key] [SISMEMBERS set_key value]
4. zset     有序集合
5. hash     hash表 [hset hash_key key value] [hget hash_key key]

#### Redis高性能的原因
1. 单线程，避免上下文切换
2. 纯内存，响应速度快
3. 非阻塞IO

### Redis 持久化方式
>RDB （Redis Database）
>文件体积小、恢复速度快、但是有丢数据的风险

>AOF（Append Only File）可以认为是日志文件
文件提交大、恢复速度慢、根据同步的策略会有不同的丢数据风险 <br/>
同步策略：
1. 修改即同步，不会丢数据， 性能较差
2. 每秒同步，宕机会丢失一秒的数据


### Redis高可用
1. 简单主从复制，replication [master写、slave读；master发送数据保持salve的更新；主节点挂了无法选举新的节点执行写操作]
2. 哨兵, Sentinel [哨兵是一个独立的进程，哨兵会实时监控master节点的状态，当master不可用时会从slave节点中选出一个作为新的master，并修改其他节点的配置指向到新的master]
        1. 监控，不断检测主从服务器是否正确
        2. 提醒，某个Redis出现故障，可以通过API向管理员和其他Redis发送通知
        3. 自动故障迁移，master坏了，会重新选举master，并且迁移。 