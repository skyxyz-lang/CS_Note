### RTT & RTO
1. RTT(Round Trip Time)：一个连接的往返时间，即数据发送时刻到接收到确认的时刻的差值；
2. RTO(Retransmission Time Out)：重传超时时间，即从数据发送时刻算起，超过这个时间便执行重传。
### TCP如何保证可靠性（通过累计确认、超时重传、拥塞控制）
1. 停止等待协议和自动重传请求 ARQ
> 具体解释为每发送完一个分组就停止等待对方确认，收到确认再发送下一个分组，如果超时没有收到确认就重传。
ARQ协议分为 停止等待ARQ协议、连续ARP协议+滑动窗口协议
2. 拥塞控制
1. 慢开始, 维护拥塞窗口，每收到一个轮次，窗口+1，第一个传输轮次，窗口翻倍，直到为ssthresh，进行拥塞避免
2. 快重传 要求接收方每收到一个时序的报文段后就立即发出重复确；发送方只要一连收到三个重复确认，就应当立即重传对方尚未收到的报文段，而不必等待设置的重传计时器到期
3. 快恢复 收到重复三个确认时，窗口从ssthresh减半开始，采用拥塞避免算法。

### 参考文献
1. https://blog.csdn.net/qq_33314107/article/details/81607630
2. https://blog.csdn.net/guoweimelon/article/details/50878503
3. https://blog.csdn.net/guoweimelon/article/details/50880109
a