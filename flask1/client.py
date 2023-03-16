#  === TCP 客户端程序 client.py ===

# 引入socket库
from socket import *

#配置项：客户端要访问的IP地址（此处是本机）、服务端程序端口号、客户端缓冲区长度
IP = '127.0.0.1'
SERVER_PORT = 50000
BUFLEN = 1024

# 实例化一个socket对象，命名为‘数据传输接口’（因为是客户端）
# 指明协议（客户端与服务器所用通信协议必须一致）
dataSocket = socket(AF_INET, SOCK_STREAM)

# 调用connect()(参数为服务端程序的IP和PORT)连接服务端正在等待的listen_socket
# 此时操作系统底层就向服务端发送三次握手的第一个报文了
# 之后服务端的concept()底层和客户端的connect()底层就开始进行三次握手
dataSocket.connect((IP, SERVER_PORT))

# =================================part 1 =====================================

while True:
    # 从终端读入用户输入的字符串
    toSend = input('>>> ')
    if  toSend =='exit':
        break
    # 发送消息，也要编码为 bytes
    dataSocket.send(toSend.encode())

    # 等待接收服务端的消息
    # 如果等不到就停在这里不动了
    recved = dataSocket.recv(BUFLEN)
    # 如果返回空bytes，表示对方关闭了连接
    if not recved:
        break
    # 打印读取的信息
    print(recved.decode())

dataSocket.close()

# =================================part 2 =====================================
